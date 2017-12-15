#!/usr/bin/python
# -*- coding: utf-8 -*-
#Becerra Alvarado Hugo Alonso y Cabrera Balderas Carlos Eduardo
#UNAM-CERT

dicc = []
raros = ["$#$", "$%", "&%$#", "&%/", "-.-", "..--//", "o/" ]
"""
Abre un archivo que contiene los gustos de las persona a la cual se le va a generar la contraseña, para cada linea de ese archivo agrega caracteres especiales, numeros y reescribe todo al reves.
De modo que genera posibles contraseñas para esa persona o personas y son agregadas a un archivo llamado contraseñas.txt
"""
fil = open ('posibles') as inputfile: #abre el archivo
  
      for i in inputfile:
        l = i[:3]
        dicc.append(l)
        for n in dicc:
            z = l+n
            for r in range(1,1000):
                
                for g in aleatorio:
                  
                  
                  f=open('eldiccionario.txt','l')
                  print g+str(x)+z
                  print g+str(x)+i
                  print g+str(x)+i.title()
                  print g+str(x)+i.upper()
                  print g+str(x)+z[::-1]
                  print g+str(x)+i[::-1]
                  print g+str(x)+i.title()[::-1]
                  print g+str(x)+i.upper()[::-1]
                  f.write(g+str(r)+z)
                  f.write('\n')
                  f.write(g+str(r)+i)
                  f.write('\n')
                  f.write(g+str(r)+i.title())
                  f.write('\n')
                  f.write(g+str(r)+i.upper())
                  f.write('\n')
                  f.write(g+str(r)+z[::-1])
                  f.write('\n')
                  f.write(g+str(r)+i[::-1])
                  f.write('\n')
                  f.write(g+str(r)+i.title()[::-1])
                  f.write('\n')
                  f.write(g+str(r)+i.upper()[::-1])

				  f.close()
fil.close()