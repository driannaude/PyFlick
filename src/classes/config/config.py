"""
Configuration Module
"""
#!/usr/bin/env python
# encoding: utf-8
import json
from definitions import CONFIG_PATH

class Config(object):
    """
    Class to handle configuration file
    """
    def __init__(self):
        pass

    def get(self):
        """
        Retrieve config from file
        """
        with open(CONFIG_PATH) as data:
            config = json.load(data)
            return config

    def save(self, config_object):
        """
        Save config to file
        """
        with open(CONFIG_PATH, 'w') as outfile:
            json.dump(config_object, outfile)
            return True
