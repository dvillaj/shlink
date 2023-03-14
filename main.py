import pathlib
import json
from shlink import Shlink

shlink = Shlink("host", "api-key")

links = shlink.list_links()

pathlib.Path("shlink.txt").write_text(json.dumps(links))

with open('shlink.txt','r') as file:
    data_JSON = file.read()
    
links = json.loads(data_JSON)

links = shlink.list_links()
for link in links:
    shortCode = link['shortCode']
    print(f"Processing {shortCode}")
    shlink.delete_link(shortCode)
    shlink.add_link(link['title'], link['longUrl'], shortCode, link['tags'])