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
    # Returns Price Per KwH
    print api.getPricePerKwh()
    # Returns dict with Charges and price 
    print api.getPriceBreakdown()
    # Get last updated timestamp
    print api.getLastUpdateTime()
    # Get last updated timestamp as seconds since epoch
    print api.getLastUpdateTime(True)
    # Get next update timestamp
    print api.getNextUpdateTime()
    # Get next update timestamp as seconds since epoch
    print api.getNextUpdateTime(True)

if __name__ == "__main__":
    main()
