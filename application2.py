#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 08:20:00 2024

@author: adamtall
"""

#creation d'une variable "username" ayant pour valeur le mot graven 
username="graven"
#creation d'une variable 'age' ayant pour valeur 19
age=19
print(username,age)
# change la valeur par 25
age =25
# affiche la nouvelle valeur
print(age)
age= age+1
age = age * age
print("salut"+username+",vous avez"+str(age)+"ans")



#recoltons la premiere note:
note1= int(input("entrer la premiere note"))
#recoltons la deuxieme note:
note2=int(input("entrer la deuxieme note"))
# recoltons la troisieme note 
note3= int(input("entrer la troisieme note"))
# caluculons la moyenne 
result=(note1+note2+note3)/note3
# affichons le resultat
print("la moyenne de l'eleve est de"+str(result))


# recoltons une valeur porte monnaie
valeur=500
#creons un produit qui aura pour valeur 50
savon=50
#affichons la nouvelle valeur du porte monnaie apres spn achat
result=valeur - savon
print("la nouvelle valeur du porte monnaie est de"+str(result))