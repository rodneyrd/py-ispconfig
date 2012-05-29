==============================================
PYISPConfig - A simple wrapper around the ISPconfig3 API
==============================================

Current Maintainer: 	

	Benjamin Bouvier <benjamin.bouvier29@gmail.com>

Original Authors: 

	Benjamin Bouvier <benjamin.bouvier29@gmail.com>


Copyright (c) 2012, Benjamin Bouvier.
All rights reserved, see the file LICENSE for conditions of use.


! VERY IMPORTANT !
====================
The remote API need updates.
Some fonction of PYISPConfig won't work until updates are made.
You just have to update the 'remoting.inc.php' file following theses steps

On the ISPconfig Server, 

	1) Go to the REMOTE API repository file:

		$ cd /usr/local/ispconfig/interface/lib/classes/

	2) Update the 'remoting.inc.php' file by the 'remoting.inc.php' in "Files" repo, or get it on "http://benjaminbouvier.fr/files/remoting.inc.txt"

       $ mv remoting.inc.php remoting-old.inc.php

       $ wget http://benjaminbouvier.fr/files/remoting.inc.txt

       $ mv remoting.inc.txt remoting.inc.php


	Detail : I just added this code, at the beginning of functions which needs dictionnaries arguments ('client_add' function  for example):

		"	
			$mytable = array();
			foreach($params as  $value){
				$mytable[$value[0]] = $value[1];
			}
			$params = $mytable ;
		"


INTRODUCTION
============

    The goal of the PYISPConfig wrapper is to provide a simple code to use
    for Python and very simple to use and that fully supports interactions between ISPConfig3 API and a Django/Python client.
    
    INCLUDED
    --------

    - SOAPpy (https://github.com/jeffkit/SOAPpy)

    
    FEATURES
    --------

    - Connexion to remote API
    - Login and Logout as remote user
    - Handles principals client's actions
    - Handles principals database's actions
    - Handles few server's actions
    
    TODO (See RELEASE_INFO and CHANGELOG for recent changes)
    ----

    - Take over all functions of the API
    
    MANIFEST
    --------
    
    Files

    
        README	        	  	This file
        pyispconfig.py        	Wrapper to use

        SOAPPy/*				SOAPpy librarie
        Files/views.py 			Simple example "How to use the Wrapper"
    	Files/remoting.inc.php	File to replace on your ISPConfig server
    

INSTALLATION
============

    REQUIRED PACKAGES:
    -----------------

    - SOAPpy 0.12.5 or later,
      <http://research.warnes.net/projects/rzope/fpconst/>

    
    INSTALLATION STEPS
    ------------------
    
    As of version 0.9.8 SOAPpy can be installed using the standard python
    package installation tools.  
    
    To install:
    
      1) Unpack the package
        
      2) Include it in a repository of your project
    
      3) Make sur SOAPpy is installed
    
    
DOCUMENTATION
=============

    QUICK START
    -----------

    A simple way to add a new client in your app:

		from SOAPpy import SOAP
		from SOAPpy import *
		from pyispconfig import PyISPconfig

	    dict = {"usertheme": "default",
	            "username": "user1",
	            "company_name": "user1",
	            "password": "user1"}

	#Connects to Soap Server
    	ispconfig_api = PyISPconfig('127.0.0.1', 'admin', 'admin')

    #Adds a new client and return the id.
	    new_client_id = ispconfig_api.client_add(dict)
	    print new_client_id 

	#Disconnects from Soap Server 
		ispconfig_api.logout()



    OTHER DOCUMENTATION
    -------------------
      
    For further information see the files views.py.

    Note that documentation is one of PYISPconfig's current weak points.
    Please help me out!


GETTING HELP
============

    REPORTING BUGS
    --------------
    
    Please send me bug reports, feature requests, patches, etc.
    At <benjamin.bouvier29@gmail.com>
    
