"""
API Interface Module
"""
#!/usr/bin/env python
# encoding: utf-8

import json
import requests
from classes.authentication.FlickAuth import FlickAuth
from definitions import FLICK_PRICE_ENDPOINT


class FlickApi(object):
    """ Flick Electric API Interface """

    def __init__(self, username, password, client_id, client_secret):
        AuthInstance = FlickAuth(username, password, client_id, client_secret)
        self.session = AuthInstance.getToken()

    def getPrice(self):
        headers = {
          "Authorization": "Bearer %s" % self.session["id_token"]
        }
        req = requests.get(FLICK_PRICE_ENDPOINT, headers=headers)
        if req.status_code is not 200:
          # If we don't get a success response, we raise an exception.
          raise Exception({
            "status": req.status_code,
            "message": req.text
          })
        # A 200OK response will contain the JSON payload.
        response = json.loads(req.text)
        return response
