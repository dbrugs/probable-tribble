from credentials import credentials_dict
from tda import auth, client
import json

token_path = credentials_dict['token_path']
api_key = credentials_dict['consumer_key']+'@AMER.OAUTHAP'
redirect_uri = credentials_dict['redirect_uri']
try:
    c = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Firefox(executable_path = "DRIVERPATH") as driver:
        c = auth.client_from_login_flow(
            driver, api_key, redirect_uri, token_path)
