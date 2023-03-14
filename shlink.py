import requests
import json

class Shlink:
    def __init__(self, host, api_key):
        self.host = host
        self.api_key = api_key

    def status(self):
        url = f"{url_host}/rest/health"

        headers = {
            "accept": "application/json",
            "X-Api-Key": self.api_key
        }
        payload = ""
        response = requests.request("GET", url, data=payload, headers=headers)

        return json.loads(response.text)

    def list_links(self):
        url = f"{self.host}/rest/v3/short-urls"
        querystring = {"itemsPerPage":"10000"}
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
            "X-Api-Key": api_key
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        return json.loads(response.text)

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