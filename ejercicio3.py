#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice

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
"""
def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])
"""
def aproxrepro():
    aprobados = []
    reprobados = []
    for alumno in calificacion_alumno:
        if (calificacion_alumno[alumno] >= 8):
            aprobados.append(alumno)
        else:
            reprobados.append(alumno)
    return tuple(aprobados),tuple(reprobados)

def promedio():
    calif=[]
    for alumno in calificacion_alumno:
        calif.append(alumno)
        return float(sum(calif))/max(len(calif),1)
        

asigna_calificaciones()
#imprime_calificaciones()
#print aproxrepro()
print promedio



