# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 08:10:42 2016

@author: Satya
"""
# creating a table in the database
import sqlite3
conn = sqlite3.connect('KnowledgeBase.db')
c = conn.cursor()

def createDB():
    c.execute("CREATE TABLE wordVals(word TEXT,value REAL)")
    c.execute("CREATE TABLE doneSyns(word TEXT,value REAL)")
    
#The idea behind scraping the words from www.thesaurus.com was to retrieve the 
#HTML page data and then parse,and extract the data.


