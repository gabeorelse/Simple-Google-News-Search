import urllib.request
import pandas as pd
from openpyxl import Workbook
from html.parser import HTMLParser
import time
from time import sleep
from random import randint 
from urllib.request import Request, urlopen
from urllib.error import URLError
import json
import pyshorteners

search = input("Enter your search: ")
page = 2

class Data_Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.is_script = False
        self.data = []
        self.head = []


    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == 'href':
                    new = attr[1]
                    self.head.append(new)
                    self.is_script = True

    def handle_endtag(self, tag):
        if tag == "a":
            self.is_script = False
    
    def handle_data(self, data):
        if self.is_script:
            self.data.append(data)
            
parse = Data_Parser()

#iterate over Google News pages 
for page in range(0, 10):
    fed_url = 'https://www.google.com/search?q={}&source=lnms&tbm=nws&start={}'.format(search, (page - 1) * 10)
    
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0'

    headers = {'User-Agent': user_agent}
    
    req = Request(fed_url, headers=headers)
    try:
        #make request, read response, print results
        response = urlopen(req)
        body = response.read().decode('utf-8')
        parse.feed(body)
        results = parse.data
        print(parse.head)
        print(results)
    #if error:
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    finally:
        print("The Program has run.")     

SEARCH = True

#basic while loop to filter results
while SEARCH:
    x = input("Would you like to search the news?\nY/N: ").lower()
    if x == "y":
        term = input("Enter a search term: ")
        result = [item for item in results if term in item]
        if result == []:
            try_again = input("No results. Would you like to try again?\nY/N: ").lower()
            if try_again == 'n':
                print("Good luck with your research!")
                break
        elif result is not None:
            print(result)
            #save to csv
            export = input("Would you like to save these results?\nY/N: ").lower()
            if export == "y":
                df = pd.DataFrame(result)
                df.to_csv('searchresults.csv', index=False)
                print("Your files are saved. Here's a preview:\n")
                print(df)
                again = input("Would you like to do another search?\nY/N: ").lower()
                if again == 'n':
                    print("Good luck with your research!")
                    break
            else:
                print("Good luck with your research!")
                break
    else: 
        print("Thanks, goodbye!")
        break

    



    



    
    

    


    
    
    

    

        
    
    



    


    

