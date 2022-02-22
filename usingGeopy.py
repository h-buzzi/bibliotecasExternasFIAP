# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 12:19:08 2022

@author: hbuzzi
"""

from geopy.geocoders import Nominatim
import os

geolocator = Nominatim(user_agent="wazeyes")

def localizar():   
    endereco=input("Digite um endereco com número e cidade. "
                   "Exemplo: avenida paulista, 100 São Paulo:") #Input com o endereço
    resultado = str(geolocator.geocode(endereco)).split(",") #Resultado transformado em string e então separado em cada informação
    
    if resultado[0]!='None': #Se retornou um resultado
        print("Endereço completo.: ", resultado)
        print("Bairro............: ", resultado[1])
        print("Cidade............: ", resultado[2])
        print("Regiao............: ", resultado[3])
        
def localiza_inv():
    latitude=float(input("Digite a latitude...: "))
    longitude=float(input("Digite a longitude.: "))
    
    resultado = str(geolocator.reverse(f"{latitude}, {longitude}")).split(",") #Usa o reverse para fazer a pesquisa inversa usando latitude e longitude, e divide o resultado em uma lista
    if resultado[0]!='None':
        print("Endereço completo.: ", resultado)
        print("Dado 1............: ", resultado[0])
        print("Dado 2............: ", resultado[1])
        print("Dado 3............: ", resultado[2])
        
escolha = 'A'
while(escolha != 'L' or escolha != 'I' or escolha != 'S'):
    escolha  = input("Escolha uma das opções:\n<L> para localizar usando um endereço\n<I> para localizar usando latitude/longitude\n<S> para sair").upper()

if escolha=='L':
    localizar()
elif escolha=='I':
    localiza_inv()
elif escolha=='S':
    os.exit()