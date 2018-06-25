#!/usr/bin/python
# coding=utf8

import sys, os, json

FILE = ""

# lecture du fichier et affichage en json
try:

    # Creation de l'objet Json
    data = {}

    #Lecture de fichier
    fichier = open("exemple.log", "r")
    for line in fichier:
        donnee = line.split(" ")
        data['0'] = donnee[0]
        data['1'] = donnee[1]
        data['2'] = donnee[2]
        data['3'] = donnee[3]
        data['4'] = donnee[4]
        data['5'] = donnee[5]
        data['6'] = donnee[6]
        data['7'] = donnee[7]
        data['8'] = donnee[8]
        data['9'] = donnee[9]

        # Creation du fichier json json_data
        json_data = json.dumps(data)

        #affichage du data jjson
        print json_data

except Exception, message:
    print "Erreur d'ouverture du fichier"
