"""
Main Module
"""
#!/usr/bin/env python
# encoding: utf-8

from classes.api.FlickApi import FlickApi
from classes.config.config import Config

def main():
    """ Main, nuff said """
    config = Config().get()
    api = FlickApi(config["username"], config["password"], config["client_id"], config["client_secret"])
    price = api.getPrice()

if __name__ == "__main__":
    main()
