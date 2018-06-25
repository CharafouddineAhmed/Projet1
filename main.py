#!/usr/bin/python
# coding=utf8

import sys, os, json, requests

from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

# lecture du fichier et affichage en json
try:

    #Lecture de fichier
    fichier = open("exemple.log", "r")
    i = 1
    for line in fichier:
        donnee = line.split(" ")
        data = {
            '0' : donnee[0],
            '1' : donnee[1],
            '2' : donnee[2],
            '3' : donnee[3],
            '4' : donnee[4],
            '5' : donnee[5],
            '6' : donnee[6],
            '7' : donnee[7],
            '8' : donnee[8],
            '9' : donnee[9],
        }

        res = es.index(index="test-index-2", doc_type='tweet', id = i, body=data)
        print(res['result'])
        i = i + 1
        # Creation du fichier json json_data
        json_data = json.dumps(data, indent=4, sort_keys=True)

        #affichage du data json
        print json_data

except Exception, message:
    print "Erreur d'ouverture du fichier"
