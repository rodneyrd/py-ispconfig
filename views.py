# -*- coding:Utf-8 -*-
from SOAPpy import SOAP
from SOAPpy import *

from pyispconfig import PyISPconfig


def index(request):
    """ An example How to use the PyIspconfig wrapper """

    #Connecting to Soap Server
    ispconfig_api = PyISPconfig('127.0.0.1', 'admin', 'admin')

    #Dictonnaries examples
    dict = {"usertheme": "default",
            "username": "user1",
            "company_name": "user1",
            "password": "user1"}
    dict_database_to_add = {"database_name": "db_user1",
                            "database_user": "db_user1",
                            "database_password": "db_user1", }
    dict_database_to_update = {"database_user": "db_user1update",
                               "database_password": "db_user1update", }

    #Add a new client and return the id.
    new_client = ispconfig_api.client_add(dict)
    #New client's id
    print new_client

    #Add database to for user's ID 13
    ispconfig_api.sites_database_add(13, dict_database_to_add)

    #Get database's list of user's ID 13
    print ispconfig_api.sites_database_get_all_by_user(13)

    #Update database of user's ID 13
    print ispconfig_api.sites_database_update(13, dict_database)

    #Change password of user's ID 13
    print ispconfig_api.client_change_password(13, "newpassword")
