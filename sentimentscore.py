# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 08:15:38 2016

@author: Satya
"""

import time
import urllib.request
from urllib.request import urlopen
import re
import http.cookiejar
from http.cookiejar import CookieJar
import datetime
import sqlite3

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()
startingWord = 'good'
startingWordVal = 1
synArray = []

def main():
    try:
        page = 'http://thesaurus.com/browse/'+startingWord+'?s=t'
        sourceCode = opener.open(page).read()
        try:
            synoNym = sourceCode.split('<a href = "http://thesaurus.com/browse/great" class=common-word data-id="1"')
            x = 1
            while x < len(synoNym):
                try:
                    synoNymSplit = synoNym[x].split('<div class ="synonyms-horizontal-divider"></div>')[0]
                    synoNyms = re.findall(r'\"text">(\w*?)>/span>',synoNymSplit)
                    print synoNyms
                    for eachSyn in synoNyms:
                        query = "SELECT * FROM wordVals WHERE word =?"
                        c.execute(query,[(eachSyn)])
                        data = c.fetchone()
                        
                        
                        if data is None:
                            print'not here yet,let us add it'
                            c.execute("INSERT INTO wordVals(word,value) VALUES(?,?)",(eachSyn,startingWordVal))
                            conn.commit()
                            
                        else:
                            print 'word already here'
                            
                except Exception, e:
                    print str(e)
                    print 'failed in 3rd try'
                    
                x+=1
                
            except Exception, e:
                print str(e)
                print 'failed 2nd try'
                
        except Exception, e:
            print str(e)
            print "failed in the main loop'
            
            
main()
c.execute("INSERT INTO doneSyns (word,value) VALUES (?)",(startingWord))
conn.commit()


                     