import pathlib
import json
from shlink import Shlink
import configparser

config = configparser.ConfigParser()
config.read('shlink.properties')

url_host=config.get("shlink", "url_host")
api_key=config.get("shlink", "api_key")

shlink = Shlink(url_host, api_key)

shlink.backup("shlink.backup")
links = shlink.restore("shlink.backup")

links = shlink.list_links()
for link in links:
    shortCode = link['shortCode']
    print(f"Processing {shortCode}")
    #shlink.delete_link(shortCode)
    #shlink.add_link(link['title'], link['longUrl'], shortCode, link['tags'])