#!/usr/bin/python
# coding=utf8

import sys, os, json, requests, yaml
from datetime import datetime
from elasticsearch import Elasticsearch


i = 1
try:

    with open("config.yml", 'r') as fichier_yml:
        cfg = yaml.load(fichier_yml)

    es = Elasticsearch("%s:%s/"%(cfg['elastic']['host'],cfg['elastic']['port']))
    #print "INFO : ", json.dumps(es.info(), indent=4, sort_keys=True)

    #Lecture de fichier
    fichier = open("%s"%(cfg['autre']['path']), "r")

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

        #res = es.index(index="test", doc_type="tweet", id = i, body=data)
        #print(res['result'])
        i = i + 1

        #affichage du data json
        #print json.dumps(data, indent=4, sort_keys=True)

    fichier.close()

except Exception, message:
    print "Erreur : ", message
    sys.exit(1)

print "PROGRAMME TERMINE"
#pip install pyyaml
