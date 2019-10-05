import requests
import json
import urllib.parse as parse
class Duck:
    def __init__(self, query):
        self.query = query
        self.result = {}
        self.base_url =  "https://api.duckduckgo.com?q=" + self.query

    def search(self):
        resp = requests.get(self.base_url, params= { "format": "json"})
        if not resp.status_code > 200:
            print(resp.text)
            self.result = json.loads(resp.text)
            return resp.url