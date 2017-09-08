"""
Authentication Module
"""
#!/usr/bin/env python
# encoding: utf-8

import json
import time
import requests
from definitions import AUTH_FILE_PATH
from classes.exception_handler.custom import AuthException

class FlickAuth(object):
    """
    Class to handle authentication/token generation
    """
    def __init__(self, username, password, client_id, client_secret):
        """
        Initialize and get an authentication token
        """
        token = self.__checkActiveSession()
        if not token:
          self.token = self.__authenticatedFlick(username, password, client_id, client_secret)
        else:
          self.token = token

    def __checkActiveSession(self):
        """
        Check for an active session and return it if it exists
        """
        with open(AUTH_FILE_PATH) as data:
            token = json.load(data)
            now = int(time.time())
            if now < token["expires_at"]:
                return token
            return False

    def __saveAccessTokenToFile(self, data):
        """
        Save the access token to file
        """
        data["authenticated_at"] = int(time.time())
        # FYI: Tokens appear to expire in 2 months/60 days
        data["expires_at"] = data["authenticated_at"] + data["expires_in"]
        with open(AUTH_FILE_PATH, 'w') as outfile:
            json.dump(data, outfile)

    def __authenticatedFlick(self, username, password, client_id, client_secret):
        """
        HTTPS Auth method
        """
        payload = {
            "grant_type": "password",
            "client_id": client_id,
            "client_secret": client_secret,
            "username": username,
            "password": password
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        req = requests.post("https://api.flick.energy/identity/oauth/token", data=payload, headers=headers)
        if req.status_code is not 200:
            # If we don't get a success response, we raise an exception.
            raise AuthException({
              "status": req.status_code,
              "message": req.text
            })
        # A 200OK response will contain the JSON payload.
        response = json.loads(req.text)
        self.__saveAccessTokenToFile(response);
        return response

    def getToken(self):
        """ Returns the token"""
        return self.token
