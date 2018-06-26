#!/usr/bin/python
# coding=utf8

import sys, os, json, yaml, time,  logging

from datetime import datetime
from elasticsearch import Elasticsearch
import logging

compteur = 1
try:

    #ouverture du fichier config
    with open("config.yml", 'r') as fichier_yml:
        cfg = yaml.load(fichier_yml)

    #Connexion avec Elasticsearch
    es = Elasticsearch("%s:%s/"%(cfg['elastic']['host'],cfg['elastic']['port']), verify_certs=True)
    if not es.ping():
        raise ValueError("Conneion avec Elasticsearch (http://%s:%s)  refusée "%(cfg['elastic']['host'],cfg['elastic']['port'] ))

    #res = es.indices.create(index=("%s"%cfg['index']['name']), ignore=400)

    #Lecture des données dans les logs
    for path, dirs, files in os.walk("%s"%(cfg['autre']['path'])):
        #Pour chaque fichier du repertoire, faire :
        for filename in files :

            fichier = open("%s/%s"%(cfg['autre']['path'],filename), "r")
            for line in fichier:
                donnee = line.split(" ")
                data = {
                    "timestamp": datetime.now(),
                    'file' : "%s"%(filename),
                    'formatLog' : "table_space",
                    'name' : donnee[0],
                    'mbytes' : float(donnee[1]),
                    'used' : float(donnee[2]),
                    'free' : float(donnee[3]),
                    'pct_used' : float(donnee[4]),
                    'largest' : float(donnee[5]),
                    'max_sixe' : float(donnee[6]),
                    'pct_max-used' : float(donnee[7]),
                    'extent_man' : donnee[8],
                    'segmen' : donnee[9],
                }

                # Creattion d'index et ajout des donnéees.

                res = es.index(index=("%s"%cfg['index']['name']), doc_type=("%s"%cfg['index']['document_type']), id = compteur, body=data)

                t = datetime.now()
                print ( '%s %s'%(t,res['result']))
                compteur = compteur + 1

                #affichage du data json
                #print json.dumps(data, indent=4, sort_keys=True)

except Exception, message:
    print "Erreur : " ,message
    sys.exit(1)

print "PROGRAMME TERMINE"
#pip install pyyaml
