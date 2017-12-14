#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

sistemas = ['angie','juan','jonatan']
op_interna = ['quintero','fernando','yeudiel']
incidentes = ['demian','anduin','diana','victor','vacante']
auditorias = ['juan','fernando','oscar','daniel','gonzalo','cristian','jorge','virgilio']


#expresion funcional:
# 1) funcion lambda que sume las cuatro listas
# 2) filtre la lista resultante para obtener todos los nombres que tienen una "i"
# 3) convierta a mayusculas el resultado anterior
#UNA SOLA EXPRESION

z=(lambda a,b,c,d:(a+b+c+d))(sistemas,op_interna,incidentes,auditorias)
#print z
x=filter(lambda nombre: 'i' in nombre,z)
#print x
w=map(lambda nombre:nombre.upper(),x)
#print w
p=(lambda s: s.join(w))(",")
print p
