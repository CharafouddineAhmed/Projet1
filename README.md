Python Elasticsearch Client
---------------------------

Client Elasticsearch en python. Ce programme permet d'indexer données de ficheirs logs (/logs/*.log) dans la base Elasticsearch.  

Dependance
-------------

.
├── config.yml           Configuration minimale à faire

├── logs

│   ├── TABLESPACE_h1a1sd211m_NETIKA_20180612-2357.log

│   ├──  ..... 

│   └── TABLESPACE_h1a1sd211m_NETIKA_20180614-1152.log

├── main.py
└── README.md

 
1.  En fonction de votre verison d'Elasticsearch :  
    Exemple (Elasticsearch V 6.X) 
        pip install elasticsearch6

2.  pip install pyyaml

NB : N'oublies pas la petite config au fichier (config.yml) 

Installation
------------

  sudo chmod 777 main.py 
  
  python ./main.c


