# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:37:43 2022

@author: hbuzzi
"""

from geopy.geocoders import Nominatim
import json
import os

def ler_arquivo(arquivo): #Função ler arquivo JSON
    if os.path.exists(arquivo): #Verifica se o caminho do arquivo existe
        with open(arquivo,'r') as arq_json: #Abre o arquivo como leitura
            dicionario = json.load(arq_json) #Usa função do json para carregar como dicionario python
    else: dicionario = {} #Se não tiver o caminho do arquivo, cria um dicionário vazio
    return dicionario #Retorna o dicionário do arquivo

def gravar_arquivo(dicionario,arquivo): #Gravar o dicionario como arquivo JSON
    with open(arquivo,'w') as arq_json: #Cria o arquivo com o nome inserido na função
        json.dump(dicionario, arq_json) #Grava o dicionario como JSON por meio da função dump
    return

geolocator = Nominatim(user_agent="wazeyes") #Nome da aplicação no geopy
dicionario=ler_arquivo("entrada.json") #Pega o dicionário do arquivo JSON
lista=dicionario["endereco"] #Pega a lista do endereço no dicionário
endereco=lista[0] + "," + lista[1] + " " + lista[2] + " " + lista[3] #Cria o endereço no formato do geocode
location = geolocator.geocode(endereco) #Encontra a localização pelo geopy
saida={"coordenadas": (location.latitude, location.longitude)} #Pega as coordenadas
gravar_arquivo(saida,"saida.json") #Grava a saída