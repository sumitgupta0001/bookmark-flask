#from mongoengine import *
#connect('tumblelog2')

import os
from mongoengine import *

final_mongo_host = "mongodb://admin:C2utndwzfJHp@%s:%s/" % (os.environ['OPENSHIFT_MONGODB_DB_HOST'], os.environ['OPENSHIFT_MONGODB_DB_PORT'])
connect('myflaskapp', host=final_mongo_host)
    #,username='admin',password='C2utndwzfJHp')

class registration(Document):
    name_db=StringField(required=True)
    
    email_db=EmailField(required=True)
    create_password=StringField(required='')
    confirm_password=StringField()


class Bookmark_db(Document):
    name=StringField(required=True)
    location=StringField(required=True)
    labels=StringField(required=True)
    notes=StringField(required=True)
    email=StringField(required=True)