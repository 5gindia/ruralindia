# -*- coding: utf-8 -*-
"""
Created on Sun May 31 00:30:51 2020

@author: Sidharth
"""


#%%
# to mark lines to between the connected fpois and gps 

# import folium package 
import folium 
import pandas as pd

dataset = pd.read_csv('sikkim_c.csv')

my_map4 = folium.Map(location = [28.5011226, 77.4099794], 
                                        zoom_start = 12) 

for i in range(len(dataset)) : 
    print(dataset.loc[i, "LAT"], dataset.loc[i, "LONG"])
    
    lat = dataset.loc[i, "LAT"]
    lng = dataset.loc[i, "LONG"]


    lat1 = dataset.loc[i, "LAT1"]
    lng1 = dataset.loc[i, "LONG1"]


  
    folium.marker([dataset.loc[i, "LAT"],dataset.loc[i, "LONG"]],icon=folium.Icon(color='green') 
              ).add_to(my_map4) 
  
    folium.marker([dataset.loc[i, "LAT1"],dataset.loc[i, "LONG1"]],icon=folium.Icon(color='red')
              ).add_to(my_map4) 
  
# Add a line to the map by using line method 
# it connect both coordiates by the line 
# line_opacity implies intensity of the line 
  
    folium.PolyLine(locations = [(lat,lng),(lat1,lng1)], 
                    
                    line_opacity = 0.5).add_to(my_map4) 
  
    my_map4.save("my_map4.html")
