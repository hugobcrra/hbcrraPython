#!/usr/bin/python
# -*- coding: utf-8 -*-
#Hugo BEcerra
#UNAM-CERT
"""

Se define la función primo, que a X le asigana un alor booleano e inicia un
for en un cierto rango, que inicia en 2 y termina en otra variable que es a,
después inicia un if donde el "a" modulo de "i" es igual a 0.
A x se le define un valor False si se cumple la condición y termina.
Se crea otra función que imprime x si este es true y te avisa que el numero es
primo, si no, un false.
Al sacar modulo (x%2) de un numero primo este debe de dar 1, asi se cumple con la condición inicial.


def primo(a):
    x = True 
    for i in range(2, a):
       if a%i == 0:
           x = False
           break 
    if x:
        print ("Es número primo")
    else:
        print ("No es número primo")
primo(9)
"""
#--------------------------------------------------------------------
x = "" #Dejamos una cadena vacia

def palindromo(s):
    if s == s[::-1] : #Primo valida la cadena, checando si es un palindromo
        return True

s = "anitalavalatinaosooooaooooooooooooo"

for a, item in enumerate(s): #Nos enumera los datos en forma de lista de la cadena S
    for b, item in enumerate(s): 
        d = s[a:b+1] #La variable d tiene la variable s que nos genera una lista con la cadena S y
                    #selecciona una posicion a esa cadena
        if palindromo(d) and (len(d) > len(x)): #llama la función palindromo y agrega la lista d, y si d tiene un largo major a x
                                                #(la cadena vacia) va a asignar x a d e imprime el palindromo más grande.
            x = d

print(x)

#---------------------------------------------------------------------
#Dar los n numeros primos

def nPrimo(num,n)
    
