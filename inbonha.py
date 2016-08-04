#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randint

maximo_silabas = 4
silabas = ['MÔ','NI','CA','CE','BO','LI','NHA','MA','GA','LI','CAS','CÃO','BI','DU','IN']
flags = [True] * len(silabas)

def numero():
	return randint(2,maximo_silabas)

def nome():
	inbonha = ''
	for i in range(numero()):
		x = randint(0,len(silabas))
		if flags[x]:
			inbonha += silabas[x]
			flags[x] = False
	
	return inbonha
	
print(nome())
	