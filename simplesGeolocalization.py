# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:34:33 2022

@author: hbuzzi
"""

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="wazeyes") # Nome da aplicação
location = geolocator.geocode("175 5th Avenue NYC") #função que localiza a partir do nome
print(location.address) #Localização adress
print((location.latitude, location.longitude)) #Localização latitude e longitude