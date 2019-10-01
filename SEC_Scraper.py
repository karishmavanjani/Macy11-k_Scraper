from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys
import re

root = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000794367&type=11-k&dateb=&owner=exclude&start=0&count=100"
results = []
url = "https://www.sec.gov"


def get_11K():
    curryear = 0
    prevyear = 0
    response = requests.get(root)
    #tell beautiful soup to parse html string
    soup = BeautifulSoup(response.text, 'html.parser')
    companyname = soup.find("span", class_="companyName").find(text=True, recursive=False)
    print(companyname)
    table = soup.find("table", class_="tableFile2")

    if table:
        rows = table.find_all("tr")[1:] #.find_all("tr")[0]
        #strip removes white space in the 
        #print(len(rows))
        for row in rows: 

            #cells = [cell.text.strip() for cell in row.find("td"[1])] 
           
            date = row.find_all("td")[3]
            stripdate= date.text.strip()[:4]
            #print(stripdate)
            curryear = stripdate 
            if curryear != prevyear: 
                documentlink = row.find_all("td")[1]
                link = documentlink.find('a')['href']
                #print(link)
                response = requests.get(url+link)
                soup2 = BeautifulSoup(response.text, 'html.parser')
                table2 = soup2.find("table", class_="tableFile")
                #print(table2)
                firstrow = table2.find_all("tr")[1]
                #for i in firstrow: 
                documentlink2 = firstrow.find_all("td")[2]
                cells = documentlink2.text.strip()
                
                #print(cells)
                link2 = documentlink2.find('a')['href']
                #print(link2) 
                response = requests.get(url+link2)  
                soup3 = BeautifulSoup(response.text, 'html.parser')
                if int(curryear)>2011:
                                        #there are multiple $ so for the list you can't find parent. 

                    table3 = soup3.find_all("font", text = re.compile('\$'))[2]
                    tbody = table3.parent.parent.find_next_sibling()
                    Final_text=tbody.text.strip()#find_all("tr")[5].
                    print(int(curryear)-1)
                    print(Final_text)
                    print("\n")
                #there is only one master trust so its a single element not a list. For the list you can't find parent. 
                    # table3 = soup3.find("font", text = re.compile('Master Trust Investments, at fair value'))
                    # tbody = table3.parent.parent.parent.parent
                    # Final_text=tbody.text.strip()#find_all("tr")[5].
                    #print(int(curryear)-1)
                    #print(Final_text)
                #print(x)
                    print("\n")
                    results.append([companyname, Final_text,int(curryear)-1])
                elif int(curryear)>2009:
                    table3 = soup3.find("font", text = re.compile('\$'))
                    #tbody = table3.parent.parent.find_next_sibling()
                    Final_text=table3.text.strip()#find_all("tr")[5].
                    print(int(curryear)-1)
                    print(Final_text)
                    print("\n")
                    results.append([companyname, Final_text,int(curryear)-1])

                else:
                    break
                #print(x)
                    
                
           
            prevyear = curryear     

            
                #soup.find()
                #print(document)
            #print(rows)
                # for i in documentlink:
                #    link= (i['href'])

                   #print(link)
                

                #         for x in rows2:
                #                 document2 = table.find("td")[2]
                        #print(document2)
                   # second_link= (i['href'])
                   # print(second_link)


                   #results.append(link)

                   #print(results)

        # else 
        #     break
            

# #make get erquest for that url
# response = requests.get(url)
# #tell beautiful soup to parse html string
# soup = BeautifulSoup(response.text, 'html.parser')
# Full_table= table.find("tbody").find_all("tr")
#  = [cell.text.strip() for cell in Full_table.find_all("td")]
# print (Full_table)



get_11K()
print(results)
df = pd.DataFrame(results,columns=["companyname","total","year"])
df.to_csv("results.csv", index= False)    

