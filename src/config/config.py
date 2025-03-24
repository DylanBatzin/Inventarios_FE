
import os
class config:
     SECRET_KEY = os.environ.get('SECRET_KEY')
 
class DevelopmentConfig(config):
     DEBUG = True
 
config = {
     'development': DevelopmentConfig
 }