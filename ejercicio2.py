#!/usr/bin/python
# -*- coding: utf-8 -*-
#Becerra Hugo
#UNAM-CERT
from random import choice
from poo1 import Becario

calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Alonso',
            'Eduardo',
            'Gerardo',
            'Rafael',
            'Antonio',
            'Fernanda',
            'Angel',
            'Itzel',
            'Karina',
            'Esteban',
            'Alan',
            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

asigna_calificaciones()
imprime_calificaciones()

objetos = []
def ejercicio():
	
	for nombre in becarios:	
	   print "Alumnos:"
    	lsta = Becario(nombre,calificacion_alumno[nombre])
		obj.append(lsta)
        print obj
        
ejercicio()