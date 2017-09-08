""" Utility Class"""
#!/usr/bin/env python
#encoding: utf-8

import json, os

class Util(object):
    """ Utility function class"""

    def __init__(self):
        pass
    
    def saveJSONFile(self, filepath, data):
        """ Saves JSON Data to File"""
        with open(filepath, 'w') as outfile:
            try:
                json.dump(data, outfile, indent=2)
            except ValueError, e:
                return False
            return True

    def getJSONFile(self, filepath):
        """ Get Data from cached file """
        if not os.path.exists(filepath):
            return False
        with open(filepath) as stream:
            data = {}
            try:
                data = json.load(stream)
            except ValueError, e:
                return False
            return data
