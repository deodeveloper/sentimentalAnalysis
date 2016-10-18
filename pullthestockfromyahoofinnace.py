# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:20:53 2016

@author: Satya
"""

import urllib.request
import time

stockToPull = 'SSNLF'

def pullData(stock):
    try:
        fileLine = stock+'.txt'
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'
                             +stock+'/chartdata;type=quote;range=1m/csv'
        sourceCode= urllib.request.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')
        
        for eachLine in splitSource:
            splitline = eachLine.split(',')
            if len(splitLine)==6:
                if 'values' not in eachLine:
                    saveFile = open(fileline,'a')
                    lineToWrite = eachLine +'n'
                    saveFile.write(lineToWrite)
        
        print 'pulled',stock
        print 'sleeping'
        time.sleep(5)
        
    except Exception,e:
        print 'main loop',str(e)
        
pullData(stockToPull)