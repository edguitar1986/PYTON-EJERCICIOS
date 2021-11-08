# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 13:07:35 2021

@author: Edgar Lincango
"""
dic1={"Raul":34,"Paula":19,"Jorge":43,"Richard":10,"Diana":3,"Isabel":76,"Gustavo":12,"Diego":37}
dic2={"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tlpC":(87,12,56,987,-61)}
dic3={"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}
dic4={"lst1":[4,6,-12,56,-9,5.7,33,100],"lst2":[9,0,81,-2,-56,],"lst3":[12,31,87,1,0,4,-11]}

print("            MENU PRINCIPAL               ")
print("Selecciones 2:ENTRAR ó 1: SALIR")
m=int(input())
while m<2:
    print("El programa a finalizado")
if m>1:
    print("Que número de diccionario desea validar, ingrese del 1 al 4")
    x=int(input())
    while x>=5 or x<1:
        print("ERROR")
        print("Que número de diccionario desea validar, ingrese del 1 al 4")
        x=int(input())
    if x==1:
        dic1={"Raul":34,"Paula":19,"Jorge":43,"Richard":10,"Diana":3,"Isabel":76,"Gustavo":12,"Diego":37}
        print("Diccionario 1:{}".format(dic1))
        a=dic1.get("Raul")
        b=dic1.get("Paula")
        c=dic1.get("Jorge")
        d=dic1.get("Richard")
        e=dic1.get("Diana")
        f=dic1.get("Isabel")
        g=dic1.get("Gustavo")
        h=dic1.get("Diego")
    
        lista=[a,b,c,d,e,f,g,h]
        for recorrido in range(1,len(lista)):
            for posicion in range (len(lista)-recorrido):
                if lista[posicion]>lista[posicion+1]:
                    temp=lista[posicion]
                    lista[posicion]=lista[posicion+1]
                    lista[posicion+1]=temp
        print("El arreglo contiene:{}elementos".format(len(lista)))
        print("Elija los valores mas altos a mostrar")
        y=int(input())
        print("Elija los valores mas bajos a mostrar")
        z=int(input())
        while (y+z)>len(lista):
            print("Los valores sobrepasan el límite del arreglo")
            print("Elija los valores mas altos a mostrar")
            y=int(input())
            print("Elija los valores mas bajos a mostrar")
            z=int(input())
        if (z+y)<=len(lista):
            if y==1:
                listay=[lista[7]]
            if y==2:
                listay=[lista[7],lista[6]]
            if y==3:
                listay=[lista[7],lista[6],lista[5]]
            if y==4:
                listay=[lista[7],lista[6],lista[5],lista[4]]
            if y==5:
                listay=[lista[7],lista[6],lista[5],lista[4],lista[3]]
            if y==6:
                listay=[lista[7],lista[6],lista[5],lista[4],lista[3],lista[2]]
            if y==7:
                listay=[lista[7],lista[6],lista[5],lista[4],lista[3],lista[2],lista[1]]
            if y==8:
                listay=[lista[7],lista[6],lista[5],lista[4],lista[3],lista[2],lista[1],lista[0]]
            if z==1:
                listaz=lista[0]
            if z==2:
                listaz=[lista[0],lista[1]]
            if z==3:
                listaz=[lista[0],lista[1],lista[2]]
            if z==4:
                listaz=[lista[0],lista[1],lista[2],lista[3]]
            if z==5:
                listaz=[lista[0],lista[1],lista[2],lista[3],lista[4]]
            if z==6:
                listaz=[lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]]
            if z==7:
                listaz=[lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6]]
            if z==8:
                listaz=[lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]]
            print("Su lista con los mayores valores es:{}".format(listay))
            print("Su lista con los menores valores es:{}".format(listaz))
            print("Selecciones 1:ENTRAR ó 2: SALIR")
    m+=1
    if x==2:
        dic2={"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tlpC":(87,12,56,987,-61)}
        print("Diccionario 2:{}".format(dic2))
        
        
    if x==3:
        dic3={"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}
        print("Diccionario 3:{}".format(dic3))
        a=dic3.get("val1")
        b=dic3.get("val2")
        c=dic3.get("val3")
        d=dic3.get("val4")
        e=dic3.get("val5")
        f=dic3.get("val6")
        g=dic3.get("val7")
        h=dic3.get("val8")
    
        lista=[a,b,c,d,e,f,g,h]
        for recorrido in range(1,len(lista)):
            for posicion in range (len(lista)-recorrido):
                if lista[posicion]>lista[posicion+1]:
                    temp=lista[posicion]
                    lista[posicion]=lista[posicion+1]
                    lista[posicion+1]=temp
        print("El arreglo contiene:{}elementos".format(len(lista)))
        print("Elija los valores mas altos a mostrar")
        y=int(input())
        print("Elija los valores mas bajos a mostrar")
        z=int(input())
        while (y+z)>len(lista):
            print("Los valores sobrepasan el límite del arreglo")
            print("Elija los valores mas altos a mostrar")
            y=int(input())
            print("Elija los valores mas bajos a mostrar")
            z=int(input())
        if (x+z)<=len(lista):
            if y==1:
                listay=[lista[7]]
            if y==2:
                listay=[lista[7],lista[6]]
            if y==3:
                listay=[lista[7],lista[6],lista[5]]
            if y==4:
                listay=[lista[7],lista[6],lista[5],lista[4]]
            if y==5:
                listay=[lista[7],lista[6],lista[5],lista[4],lista[3]]
            if y==6:
                listay=[lista[7],lista[6],lista[5],lista[4],lista[3],lista[2]]
            if y==7:
                listay=[lista[7],lista[6],lista[5],lista[4],lista[3],lista[2],lista[1]]
            if y==8:
                listay=[lista[7],lista[6],lista[5],lista[4],lista[3],lista[2],lista[1],lista[0]]
            if z==1:
                listaz=lista[0]
            if z==2:
                listaz=[lista[0],lista[1]]
            if z==3:
                listaz=[lista[0],lista[1],lista[2]]
            if z==4:
                listaz=[lista[0],lista[1],lista[2],lista[3]]
            if z==5:
                listaz=[lista[0],lista[1],lista[2],lista[3],lista[4]]
            if z==6:
                listaz=[lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]]
            if z==7:
                listaz=[lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6]]
            if z==8:
                listaz=[lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]]
            print("Su lista con los mayores valores es:{}".format(listay))
            print("Su lista con los menores valores es:{}".format(listaz))
        
    if x==4:
        dic4={"lst1":[4,6,-12,56,-9,5.7,33,100],"lst2":[9,0,81,-2,-56,],"lst3":[12,31,87,1,0,4,-11]}
        print("Diccionario 4:{}".format(dic4))
            
           



    

    
