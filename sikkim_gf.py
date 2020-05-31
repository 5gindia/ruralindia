# -*- coding: utf-8 -*-
"""
Created on Sun May 31 00:24:07 2020

@author: Sidharth
"""


#%%
# to put different markers at gps and fpois respectively

import pandas as pd
from flask import Flask,jsonify

dataset = pd.read_csv('sikkim_gp.csv')
lat = dataset['LAT']
lng = dataset['LONG']

dataset1 = pd.read_csv('sikkim_fpoi.csv')
lat1 = dataset1['LAT']
lng1 = dataset1['LONG']


print(len (lat))
print(len (lng1))

app = Flask(__name__)


@app.route('/')
def hello_world():
    ##return('hello')
    with open('sikkim_gf.html', 'r') as f:
        html_string = f.read()
    ##html_string="hello"
    return html_string

@app.route('/sikkim')
def state_name():
   return'state name'


@app.route('/gp')
def hello():
    data=[]
    for x in range(0,len(lat),1):
        data.append({"lat":lat[x],"lng":lng[x]})


    return jsonify (data) # Returns HTTP Response with {"hello": "world"}

@app.route('/fpoi')
def hello1():
    data1=[]
    for x in range(0,len(lat1),1):
        data1.append({"lat":lat1[x],"lng":lng1[x]})


    return jsonify (data1) # Returns HTTP Response with {"hello": "world"}

   
if __name__ == '__main__':
   app.run()
#%%
