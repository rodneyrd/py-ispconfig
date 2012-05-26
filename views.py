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
    new_client = ispconfig_api.client_add(0, dict)
    # print new_client = New client's id

    new_client
    print "return of client_get_id : "
    print ispconfig_api.client_get_id(1)
    """

    """
    resp = ispconfig_api.sites_database_update(3,dict_database)
    database = ispconfig_api.sites_database_get(3)
    """

    #ispconfig_api.sites_database_add(13,dict_database_to_add)
    #print ispconfig_api.client_get_id(0)
    #ispconfig_api.sites_database_add(13)
    #print ispconfig_api.sites_database_get_all_by_user(13)
    #resp = ispconfig_api.client_change_password(8,"brush")
    #print ispconfig_api.server_get_serverid_by_ip("109.239.144.60")

    return render_to_response('nsadmin/ispconfig/ispconfig_manager.html',
        locals(),
        context_instance=RequestContext(request))
    """

