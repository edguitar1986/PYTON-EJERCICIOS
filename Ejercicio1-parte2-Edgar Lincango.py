# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 20:33:12 2021

@author: Edgar Lincango
"""

print("Programa que identifica el tipo de dato de un valor ingresado por el usuario, se realizarán cinco interacciones")


print("PRIMERA INTERACCION")
print("Ingrese el primer dato:")
var1=input()

print("SEGUNDA INTERACCION")
print("Ingrese el primer dato:")
var2=input()

print("TERCERA INTERACCION")
print("Ingrese el primer dato:")
var3=input()

print("CUARTA INTERACCION")
print("Ingrese el primer dato:")
var4=input()

print("QUINTA INTERACCION")
print("Ingrese el primer dato:")
var5=input()

a=type(var1)
b=type(var2)
c=type(var3)
d=type(var4)
e=type(var5)

print("El dato {} es tipo {}".format(var1,a)) 
print("El dato {} es tipo {}".format(var2,b)) 
print("El dato {} es tipo {}".format(var3,c)) 
print("El dato {} es tipo {}".format(var4,d)) 
print("El dato {} es tipo {}".format(var5,e)) 