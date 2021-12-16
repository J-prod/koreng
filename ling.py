##IMPORTANT MESSAGE: As mentioned in the README file, ALL credits in terms of content of the bot and the research done to create these Korean-English translation and pronunication goes to the websites I am mentioning in my comments and in my project. Please visit their website for more information. 

import json
import requests
from bs4 import BeautifulSoup

#SCRAPE 2 Ling-app website for 55 basic phrases 

#step 2.1: scrape tables from the single html page-get url

url="https://ling-app.com/ko/basic-words-and-phrases-in-korean/" #this is the url to the website where I'm collecting Korean words with English definitions and romanticized pronunciation
s = requests.get(url)

    #step 2.2: data needed are in wp-block-table element, extract data only from that element using BeautifulSoup

soup=BeautifulSoup(s.text, features="html.parser")
all_figure2 = soup.find_all("figure",{'class':'wp-block-table is-style-stripes'}) #look for all class=wp-block-table which contains the tables I intend to scrape from the page

all_data2=[]
for a_figure in all_figure2:

    all_headers2 = a_figure.find_all("th")#pull out the table headers (get all th's)

    header_names2 =[]
    for header in all_headers2:
        just_text = header.text
        header_names2.append(just_text)
        
    if len(header_names2)==0:#if length of header name is 0 assign header name manually-this is necessary as there is a table without headers
      header_names2=['Korean','Pronunciation','English']
    ##need to say if header is not there, then remove first row of table 

    #populate header names with JUST the header text

    ling_table_data_row = a_figure.find_all("tr") #get all rows (get all tr's)
    for a_row in ling_table_data_row: #loop through all tr to get each data (get all td's)

        ling_table_data_tds= a_row.find_all("td") #get all td's

        if len(ling_table_data_tds)==0:
            continue

        data ={} #make a dictionary
            
        for idx,a_td in enumerate(ling_table_data_tds): #Index in for-loop to define which position refers to which header
            just_text = a_td.text 
            header_name2 = header_names2[idx]

            data[header_name2]=just_text #use header as reference for dictionary names 

        print(data) #test print dictionary

            #STEP 1.3: Add data to all list
        all_data2.append(data) #add data to all list

with open('lingkoreanwords.json','w') as koreng_dictionary_file2:
   json.dump(all_data2, koreng_dictionary_file2,indent=2)
    