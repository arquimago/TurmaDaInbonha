#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randint

maximo_silabas = 4
silabas = ['MÔ','NI','CA','CE','BO','LI','NHA','MA','GA','LI','CAS','CÃO','BI','DU','IN']
flags = [True] * len(silabas)

def numero_silabas():
	return randint(2,maximo_silabas)

def nome():
	inbonha = ''
	for i in range(numero_silabas()):
		x = randint(0,len(silabas)-1)
		if flags[x]:
			inbonha += silabas[x]
			flags[x] = False
			if x == 1 or x == len(silabas)-1:
				flags[len(silabas)-1] = False
				flags[1] = False
	return inbonha
	
print(nome())
	