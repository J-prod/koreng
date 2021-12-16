##IMPORTANT MESSAGE: As mentioned in the README file, ALL credits in terms of content of the bot and the research done to create these Korean-English translation and pronunication goes to the websites I am mentioning in my comments and in my project. Please visit their website for more information. 

import json
import requests
from bs4 import BeautifulSoup

#SCRAPE 1 Koreanly website for 1000 most common korean words - This one has the most detailed comments, rest will have comments where new code is introduced

    #step 1.1: scrape tables from the single html page-get url

url="https://koreanly.com/most-common-korean-words/" #this is the url to the website where I'm collecting Korean words with English definitions and romanticized pronunciation
r = requests.get(url)

    #step 1.2: data needed are in wp-block-table element, extract data only from that element using BeautifulSoup

soup=BeautifulSoup(r.text, features="html.parser")
all_figure = soup.find_all("figure",{'class':'wp-block-table'}) #look for all class=wp-block-table which contains the tables I intend to scrape from the page

all_data=[]
for a_figure in all_figure:

    all_headers = a_figure.find_all("th")#pull out the table headers (get all th's)

    header_names =[]
    for header in all_headers:
        just_text = header.text
        header_names.append(just_text)
        
    if len(header_names)==0:#if length of header name is 0 assign header name manually-this is necessary as there is a table without headers
        header_names=['English','Korean','Pronunciation']
          

        #populate header names with JUST the header text

    kword_table_data_row = a_figure.find_all("tr") #get all rows (get all tr's)
    for a_row in kword_table_data_row: #loop through all tr to get each data (get all td's)

        kword_table_data_tds= a_row.find_all("td") #get all td's

        if len(kword_table_data_tds)==0:
            continue

        data ={} #make a dictionary
            
        for idx,a_td in enumerate(kword_table_data_tds): #Index in for-loop to define which position refers to which header
            just_text = a_td.text 
            header_name = header_names[idx]

            data[header_name]=just_text #use header as reference for dictionary names 

        print(data) #test print dictionary
        #STEP 1.3: Add data to all list
        all_data.append(data) #add data to all list


    with open('koreanwords.json','w') as koreng_dictionary_file:
        json.dump(all_data, koreng_dictionary_file,indent=2)
