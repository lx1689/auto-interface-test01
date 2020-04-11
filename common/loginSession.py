import json

import requests

import readConfig

sessionRequest = requests.session()
# payload = {"loginname":"17644444444","loginpwd":"vip17644444444","userFlage":"1"}
payload = readConfig.ReadConfig().get_login_user('payload')
sessionRequest.post(url="https://pre2sellermall.gree.com/mobile-seller/login", json=json.loads(payload))