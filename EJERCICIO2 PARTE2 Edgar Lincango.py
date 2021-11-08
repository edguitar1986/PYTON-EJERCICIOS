# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:23:29 2021

@author: EDGAR LINCANGO
"""

print("      Elección de caracteres para su contraseña    ".upper())
print("Eliga al menos:")
print("Una letra:","K","L","M","N","O","P","Q","R","S","T")
print("Una letra:","a","b","c","d","e","f","g","h","i","j")
print("Un número:","0","1","2","3","4","5","6","7","8","9")
print("Una símbolo:","$","&","*","@")


print("Por favor ingrese su contraseña")
a=input()

if len(a)>=5 and len(a)<=15:
    cont1=0
    cont2=0
    cont3=0
    cont4=0
    for con in a:
        if con=="K" or con=="L" or con=="M" or con=="N" or con=="O" or con=="P" or con=="Q" or con=="R" or con=="S" or con=="T": 
            cont1+=1
        else:
            cont1==-1
    
    for con1 in a:
        if con1=="a" or con1=="b" or con1=="c" or con1=="d" or con1=="e" or con1=="f" or con1=="g" or con1=="h" or con1=="i" or con1=="j": 
            cont2+=1
        else:
            cont2==-1

    for con2 in a:
        if con2=="0" or con2=="1" or con2=="2" or con2=="3" or con2=="4" or con2=="5" or con2=="6" or con2=="7" or con2=="8" or con2=="9": 
            cont3+=1
        else:
            cont3==-1

    for con3 in a:
        if con3=="$" or con3=="&" or con3=="*" or con3=="@": 
            cont4+=1
        else:
            cont4==-1
    
    if cont1>=1 and cont2>=1 and cont3>=1 and cont4>=1 :
        print("Su contraseña {} es valida".format(a))
    else:
        print("Su contraseña {} tiene ERROR en la elección de caracteres".format(a))
else:
    print("ERROR: Su contraseña debe tener entre 5 a 15 caracteres")



    



