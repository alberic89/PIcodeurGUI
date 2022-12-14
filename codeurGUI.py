#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import webbrowser

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

def callback():
   webbrowser.open_new_tab('https://alberic89.github.io/PIcodeurGUI/')
   
def isit(*args):
	root.title('CodeurGUI - '+ variable.get())
	if variable.get() == 'Morse':
		try :
			f3.place_forget()
			f3_1.pack_forget()
			f2.place_forget()
		except :
			pass
		
		f3_1.place(x=425, y=5)
		f3_1.pack_propagate(False)
		checkbutton.pack(expand=True)
		
	elif variable.get() == 'César':
		try :
			f3.place_forget()
			f3_1.place_forget()
			f2.place_forget()
		except :
			pass

		f2.place(x=425, y=5)
		f2.pack_propagate(False)
		spin1.pack(expand=True)
		spin2.pack(expand=True)
	elif variable.get() == 'Vigenère':
		try :
			f3.place_forget()
			f3_1.place_forget()
			f2.place_forget()
		except :
			pass
		f3.place(x=425, y=5)
		f3.pack_propagate(False)
		clee.pack(expand=True)

def launch():
	sortie.delete(1.0, 'end')
	if variable.get() == 'Morse':
		try :
			sortie.insert(1.0, morse(entree.get(1.0, END+"-1c"), p='.',t='-',e='/',r=is_r.get(), esrom=is_esrom.get()))
		except:
			messagebox.showwarning('CodeurGUI - Erreur', 'Une erreur c\'est produite, veuillez entrer des chaînes de caractère valide, ou un ti vaut ".", un ta vaut "-" et les espaces valent "/".\nSi le problème persiste, merci d\'envoyer un rapport de bug.')
	if variable.get() == 'César':
		try :
			sortie.insert(1.0, cesar(entree.get(1.0, END+"-1c"), spin1.get(), spin2.get(), r=is_r.get()))
		except:
			messagebox.showwarning('CodeurGUI - Erreur', 'Une erreur c\'est produite, veuillez entrer des chaînes de caractère valide dans la zone de texte, ainsi que UNE seule lettre MAJUSCULE dans les deux champs en haut.\nSi le problème persiste, merci d\'envoyer un rapport de bug.')
	if variable.get() == 'Vigenère':
		try :
			sortie.insert(1.0, vigenere(entree.get(1.0, END+"-1c"), clee.get(), r=is_r.get()))
		except :
			messagebox.showwarning('CodeurGUI - Erreur', 'Une erreur c\'est produite, veuillez entrer des chaînes de caractère valide dans la zone de texte, ainsi qu\'une clef valide.\nSi le problème persiste, merci d\'envoyer un rapport de bug.')

def opentxtfile():
	pathfile = filedialog.askopenfilename(title="Ouvrir un fichier texte", filetypes=(("fichiers texte","*.txt"), ("tous les fichiers","*.*")))
	try :
		txtfile = open(pathfile,'r')
		entree.delete(1.0, 'end')
		entree.insert(1.0,txtfile.read())
		txtfile.close()
	except :
		pass

def savetxtfile():
	try :
		pathfile = filedialog.asksaveasfilename(title='Sauver la sortie dans un fichier', filetypes=(("fichiers texte","*.txt"), ("tous les fichiers","*.*")))
		txtfile = open(pathfile,'w')
		txtfile.write(sortie.get(1.0, END+"-1c"))
		txtfile.close()
	except :
		pass

def efface():
	if messagebox.askokcancel('Effacement - CodeurGUI', 'Êtes-vous sûr de vouloir tout effacer ?') :
		sortie.delete(1.0, 'end')
		entree.delete(1.0, 'end')

def askexit():
	if messagebox.askokcancel('Quitter - CodeurGUI', 'Voulez-vous vraiment quitter ?') :
		root.quit()

def apropos():
	gui = Toplevel(root)
	gui.title('À propos - CodeurGUI')
	window_width = 300
	window_height = 60
	center_x = int(screen_width/2 - window_width / 2)
	center_y = int(screen_height/2 - window_height / 2)
	gui.geometry(str(window_width)+'x'+str(window_height)+'+'+str(center_x)+'+'+str(center_y))
	l1 = Label(gui, text='À propos de CodeurGUI :')
	bt1 = Button(gui, text='https://alberic89.github.io/PIcodeurGUI/', command=callback)
	
	l1.pack()
	bt1.pack()

root = Tk()

window_width = 700
window_height = 503

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(str(window_width)+'x'+str(window_height)+'+'+str(center_x)+'+'+str(center_y))
try :	
	root.iconphoto(True, PhotoImage(file='icon.png'))
except :
	pass

OptionList = ('César', 'Vigenère', 'Morse')
variable = StringVar(root)
variable.set(OptionList[0])
is_esrom=IntVar()
is_r=IntVar()

froot = Frame(root, width =700, height =80)
f1 = LabelFrame(froot, text='Sélectionnez votre code :', width =250, height =75)
f2 = LabelFrame(froot, text='Sélectionnez le type de code César :', width =250, height =75)
f3 = LabelFrame(froot, text='Entrez la clef du Vigenère :', width =250, height =75)
f3_1=LabelFrame(froot, text='Est-ce un Esrom ?', width =250, height =75)
f4 = LabelFrame(root, text='Entrez le message :')
f5 = LabelFrame(root, text='Sortie :')
f6 = LabelFrame(root, text='Lancez le décodage :')

opt = OptionMenu(f1, variable, *OptionList)
checkbutton = Checkbutton(f3_1, text="Esrom", variable=is_esrom, onvalue=True, offvalue=False, height=2)
checkbutton2 = Checkbutton(f6, text="Décoder", variable=is_r, onvalue=True, offvalue=False, height=2)
spin1 = Spinbox(f2, values = ('Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'))
spin2 = Spinbox(f2, values = ('Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'))
clee = Entry(f3)
entree = Text(f4, height = 8)
sortie = Text(f5, height = 8)
startbt = Button(f6, text="Coder/Décoder", command=launch)

# créer un menu
menubar = Menu(root)
# créer un sous-menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Effacer", command=efface)
filemenu.add_separator()
filemenu.add_command(label="Ouvrir", command=opentxtfile)
filemenu.add_command(label="Sauvegarder", command=savetxtfile)
menubar.add_cascade(label="Fichier", menu=filemenu)
menubar.add_command(label="Quitter !", command=askexit)
menubar.add_command(label="À propos", command=apropos)
# afficher le menu
root.config(menu=menubar)

def main():	
	
	froot.pack(side=TOP)
	froot.pack_propagate(False)
	f1.place(x=25, y=5)
	f1.pack_propagate(False)
	f2.place(x=425, y=5)
	f2.pack_propagate(False)
	f4.pack()
	f5.pack()
	f6.pack()
	
	opt.pack(expand=True)
	spin1.pack(expand=True)
	spin2.pack(expand=True)
	entree.pack()
	sortie.pack()
	checkbutton2.pack()
	startbt.pack()
	
	variable.trace("w", isit)
	root.title('CodeurGUI - '+ variable.get())
	
	root.mainloop()

if __name__ == '__main__':
	main()
