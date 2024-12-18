"""Shlink class"""
import requests
import json

class Shlink:
    def __init__(self, host, api_key):
        self.host = host
        self.api_key = api_key

    def status(self):
        url = f"{self.host}/rest/health"

        headers = {
            "accept": "application/json",
            "X-Api-Key": self.api_key
        }
        payload = ""
        response = requests.request("GET", url, data=payload, headers=headers)

        return json.loads(response.text)

    def list_links(self):
        url = f"{self.host}/rest/v3/short-urls"
        querystring = {"itemsPerPage":"100000"}
        headers = {
            "accept": "application/json",
            "X-Api-Key": self.api_key
        }
        payload = ""

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        return json.loads(response.text)['shortUrls']['data']

    def add_link(self, title, longUrl, customSlug, tags):
        url = f"{self.host}/rest/v3/short-urls"
        payload = {
            "longUrl": longUrl,
            "customSlug": customSlug,
            "tags": tags,
            "title": title,
            "crawlable": False,
            "forwardQuery": True,
            "findIfExists": True
        }

        headers = {
            "accept": "application/json",
            "X-Api-Key": self.api_key
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        return json.loads(response.text)


    def get_link(self, sort_url):
        url = f"{self.host}/rest/v3/short-urls/{sort_url}"
        payload = ""
        headers = {
            "accept": "application/json",
            "X-Api-Key": self.api_key
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        return json.loads(response.text)

    def is_valid(self, sort_url):
        from urllib.parse import urlparse

        link = self.get_link(sort_url)
        longUrl = link['longUrl']
        
        try:
            result = urlparse(longUrl)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False


    def backup(self, file):
        import pathlib

        links = self.list_links()
        pathlib.Path(file).write_text(json.dumps(links))

    def restore(self, file):
        with open(file,'r') as file:
            data_JSON = file.read()
            
        return json.loads(data_JSON)


    def delete_link(self, short_url):
        url = f"{self.host}/rest/v3/short-urls/{short_url}"

        payload = ""

        headers = {
            "accept": "application/json",
            "X-Api-Key": self.api_key
        }

        response = requests.request("DELETE", url, data=payload, headers=headers)
        if response.status_code == 404:
            return json.loads(response.text)