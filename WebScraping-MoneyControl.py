#!/usr/bin/env python
# coding: utf-8

# In[2]:


from urllib.request import urlopen as URL
import bs4
from bs4 import BeautifulSoup as BS

#Created a tuple for which need to scrape



GetURL = ("https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT",
"https://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS")
#Blank List to store values
printlist = []
for eachURL in GetURL:
    
    html = URL(eachURL)
    HTML=html.read()

    GetHTMLData = BS(HTML, 'lxml')

    title = GetHTMLData.title
#print(title)
    text = title.get_text()
    printlist.append(text)

    rows = GetHTMLData.find_all('span')

    for row  in rows:
            Price_Item = row.get("id")
    
            if (Price_Item == "Bse_Prc_tick") or (Price_Item =="Nse_Prc_tick"):
                        
                value = Price_Item+"="+row.get_text()
                printlist.append(value)
                #print(row.text)
                #print(row.get_text())

for each in printlist:
    print(each)

print("\nDone")



# In[ ]:





# In[ ]:




