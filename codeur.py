#!/usr/bin/env python
# -*- coding: utf-8 -*-

def standarise(msg, d=False):
	w_letters = ("eéèëê","aàâä","oôö","uùüû","iïî","cçĉ","jĵ","hĥ","gĝ","wẅŵ","zẑ","yŷÿ","tẗ","xẍ")
	msg = msg.lower()
	for i in range(len(w_letters)):
		c = w_letters[i]
		for l in range(1,len(c)):
			msg = msg.replace(c[l],c[0])
	msg = msg.upper()
	if d :
		alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		thiskey = ''
		for i in range(len(msg)):
			if msg[i] in alpha:
				thiskey = thiskey + msg[i]
		msg = thiskey
	return msg
	
def cesar(msg, cclair, ccode, r=False):
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	msg = standarise(msg)
	if r :
		decalage = alpha.index(cclair) - alpha.index(ccode)
	else:
		decalage = alpha.index(ccode) - alpha.index(cclair)
	
	for i in range(len(msg)):
		if msg[i] in alpha :
			key = alpha.index(msg[i]) + decalage
			if key > 25:
				key -= 26
			elif key < 0:
				key += 26
			msg = msg[:i] + alpha[key] + msg[i+1:]
	return msg

def vigenere(msg, masterkey, r=False):
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	masterkey = standarise(masterkey, d=True)
	key = list(masterkey)
	c = 0
	msg = standarise(msg)
	for i in range(len(msg)):
		if msg[i] in alpha :
			if r == True:
				l = alpha.index(msg[i]) - alpha.index(key[c])
				if l < 0:
					l += 26
			else :
				l = alpha.index(msg[i]) + alpha.index(key[c])
				if l > 25:
					l -= 26
			msg = msg[:i] + alpha[l] + msg[i+1:]
			c +=1
			if c >= len(key):
				c = 0
	return msg

def morse(msg, p='.',t='-',e='/',r=False, esrom=False):
	morsedict = { 'A':'.-/', 'B':'-.../', 
                    'C':'-.-./', 'D':'-../', 'E':'./', 
                    'F':'..-./', 'G':'--./', 'H':'..../', 
                    'I':'../', 'J':'.---/', 'K':'-.-/', 
                    'L':'.-../', 'M':'--/', 'N':'-./', 
                    'O':'---/', 'P':'.--./', 'Q':'--.-/', 
                    'R':'.-./', 'S':'.../', 'T':'-/', 
                    'U':'..-/', 'V':'...-/', 'W':'.--/', 
                    'X':'-..-/', 'Y':'-.--/', 'Z':'--../', 
                    '1':'.----/', '2':'..---/', '3':'...--/', 
                    '4':'....-/', '5':'...../', '6':'-..../', 
                    '7':'--.../', '8':'---../', '9':'----./', 
                    '0':'-----/', '.':'/', ' ':'/', '\n':'/'}
	w_letters = ("eéèëê","aàâä","oôö","uùüû","iïî","cçĉ","jĵ","hĥ","gĝ","wẅŵ","zẑ","yŷÿ","tẗ","xẍ")
	if esrom :
		morsedict = { 'A':'-./', 'B':'...-/', 
                    'C':'.-.-/', 'D':'..-/', 'E':'./', 
                    'F':'.-../', 'G':'.--/', 'H':'..../', 
                    'I':'../', 'J':'---./', 'K':'-.-/', 
                    'L':'..-./', 'M':'--/', 'N':'.-/', 
                    'O':'---/', 'P':'.--./', 'Q':'-.--/', 
                    'R':'.-./', 'S':'.../', 'T':'-/', 
                    'U':'-../', 'V':'-.../', 'W':'--./', 
                    'X':'-..-/', 'Y':'--.-/', 'Z':'..--/', 
                    '9':'.----/', '8':'..---/', '7':'...--/', 
                    '6':'....-/', '5':'...../', '4':'-..../', 
                    '3':'--.../', '2':'---../', '1':'----./', 
                    '0':'-----/', '.':'/', ' ':'/', '\n':'/'}
	if r :
		result=''
		def get_key(val):
			for key, value in morsedict.items():
				if val == value:
					return key
		if p != '.':
			msg = msg.replace('.',p)
		if t != '-':
			msg = msg.replace('-',t)
		if e != '/':
			msg = msg.replace('/',e)
		v = msg.find('/')
		while v != -1 :
			l = msg[:v+1]
			result += get_key(l)
			msg = msg [v+1:]
			v = msg.find('/')
		result = result.replace('.',' ')
		result = result.replace('   ','	')
		result = result.replace('  ',' .')
		return result
	else :	
		msg = standarise(msg)
		tmsg = tuple(msg)
		msg = ''
		for i in range(len(tmsg)):
			if tmsg[i] in morsedict.keys() :
				msg += morsedict[tmsg[i]]
		if p != '.':
			msg = msg.replace('.',p)
		if t != '-':
			msg = msg.replace('-',t)
		if e != '/':
			msg = msg.replace('/',e)
		return msg

"""
Fonction non terminée.

def chiffre(msg, cclair, ccode, r=False):
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	msg = standarise(msg)
	if cclair in alpha and ccode.isdigit() and r == False:
		decalage=int(ccode)-alpha.index(cclair)
		i = 0
		while i < len(msg):
			if msg[i] in alpha :
				l = alpha.index(msg[i]) + decalage
				if l > 26:
					l -= 26
				elif l < 1:
					l += 26
				msg = msg[:i] + str(l) + ' ' + msg[i+1:]
			i += 1
		return msg
	elif cclair in alpha and ccode.isdigit() and r == True:
		decalage= -int(ccode)-alpha.index(cclair)
		alphat = tuple(alpha)
		numt = ('1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10 ','11 ','12 ','13 ','14 ','15 ','16 ','17 ','18 ','19 ','20 ','21 ','22 ','23 ','24 ','25 ','26 ')
		i=0
		result = ''
		while msg != '':
			if msg[:msg.find(' ')+1] in numt :
				l = numt.index(msg[:msg.find(' ')+1])
				l += decalage
				if l > 25:
					l -= 26
				elif l < 0:
					l += 26
				result += alphat[l]
				try :
					msg = msg[msg.find(' ')+1:]
				except IndexError :
					msg = ''
			else:
				result += msg[:1]
			try :
				msg = msg[1:]
			except IndexError :
				msg = ''
		return result
	else :
		raise ValueError("Les clées entrées ne sont pas valides. Veuillez entrer des clées sous la forme chiffre('msg', 'UNE lettre MAJUSCULE et non-accentuée', 'nombre compris entre 1 et 26 inclus', r=True si vous voulez décoder)\nExemple : chiffre('Hello, world !', 'D', '7') =>'13 10 17 17 20 , 2 20 23 17 9  !'")
"""
