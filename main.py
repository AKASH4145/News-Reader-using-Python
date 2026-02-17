import requests

a=input("Enter the topic :")
b=int(input("Enter the year you wanna read the news from :"))
c=int(input("Enter the month:"))
d=int(input("Enter the date:"))
e="0ec53475c93a48669c1b14eb3810c311"

if(b<2025 or c<11 or d<=12):
     print("Sorryy !! we only provide news from 2025-11-13 .. ")
     

else:    
     url=requests.get(f"https://newsapi.org/v2/everything?q={a}&from={b}-{c}-{d}&sortBy=publishedAt&apiKey={e}") 

data=url.json()    
Articles=data["articles"]


for i in Articles:
     
     print(i["title"] ) 
     print("\n", i["url"])
     print("\n******************************************************************\n")