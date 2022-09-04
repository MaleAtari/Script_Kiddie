from configparser import ConfigParser
import os


def make_file_path(name):
    directory = os.path.dirname(__file__)
    abs_path = os.path.join(directory, name)
    return abs_path
    
config_path = make_file_path('config.cfg')

config = ConfigParser()

#Load configuration file
config.read(config_path)



class Config:
    def __init__(self):
        self.url = config.get('VICTIM', 'url')
        self.error = config.get('VICTIM', 'error')
        self.chars = config.get('ATTACK', 'chars')
        self.chars_length = int(config.get('ATTACK', 'length'))
        self.static = str(config.get('ATTACK', 'static_text'))
        
        



