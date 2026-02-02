import configparser

config = configparser.ConfigParser()
config.read("config.ini")

def get_config(key):
    return config.get("env", key)