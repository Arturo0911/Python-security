#!/usr/bin/python3

from urllib.request import urlopen
from urllib.request import Request
from urllib.error import HTTPError
import getopt
import sys
import os
from bs4 import BeautifulSoup


class Scrap:

    def __init__(self):
        self.args = sys.argv[1:]
        self.base = None
        self.data_parsed = None
        self.emails = list()

    def _usage(self):
        print("The goal of this project is get any tag information about the web page scanned ")
        print("The tag -u or --url you must to include the url to scan <https://wherever.com>  ")
    

    def _errors(self):
        print(""" Using urllib.request.urlopen() to open a website when crawling, and encounters “HTTP Error 403: Forbidden”. 
                It possibly due to the server does not know the request is coming from. Some websites will verify the UserAgent 
                in order to prevent from abnormal visit. So you should provide information of your fake browser visit.""")


    def find_into_url(self, url):
        
        """
            Methods
            findAll(tag, attributes, recursive, text, limit, keywords)
            find(tag, attributes, recursive, text, keywords)
        """
        try: 
            with urlopen(url) as f:

                self.base = BeautifulSoup(f,"html.parser")
                #print(self.base.findAll('a'))
                self.data_parsed = self.base.findAll('span')
                #print(self.data_parsed)    
                for x in self.data_parsed:

                    if x.get_text() != "":
                    
                        print(x.get_text(), "his type")
        except HTTPError as e:

            if str(e) == "HTTP Error 403: Forbidden":
                self._errors()
            else:
                print(str(e))
    
    def show_user_agent(self, url):

        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
            request = Request(url = url, headers = headers)
            with urlopen(request).read() as f:
                print(f.reead(100).decode('utf-8'))

        except Exception as e:
            print(str(e))


    def initializr(self):
        
        try:
            
            opt, args = getopt.getopt(self.args, "hu:a:",["help", "url=", "agent="])
            #print(opt)

            for o,a in opt:

                if o in ('-u', '--url'):
                    self.find_into_url(a)
                    
                    """if self.find_into_url(a) is None:
                        print("Data cannot be founded")
                    else:
                        self.find_into_url(a)
                        print("[*]  ...Finished")"""

                if o in ('-h', '--help'):
                    self._usage()

                if o in ('-a', '--agent'):
                    self.show_user_agent(a)

        except getopt.error as e:
            print(str(e))


if __name__ == '__main__':

    scrap = Scrap()
    scrap.initializr()
