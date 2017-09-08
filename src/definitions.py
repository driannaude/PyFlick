"""
Global Constant Definition Module
"""
#!/usr/bin/env python
# encoding: utf-8

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.json')
AUTH_FILE_PATH = os.path.join(ROOT_DIR, 'auth.json')

FLICK_PRICE_ENDPOINT = "https://api.flick.energy/customer/mobile_provider/price";
