from shlink import Shlink
import dotenv
import os

dotenv.load_dotenv()


url_host=os.environ.get("shlink.url")
api_key=os.environ.get("shlink.api.key")

shlink = Shlink(url_host, api_key)

print(f"Status {shlink.status()}")

#shlink.backup("shlink.backup")
#links = shlink.restore("shlink.backup")

links = shlink.list_links()
for n, link in enumerate(links):
    shortCode = link['shortCode']
    print(f"Processing {n + 1} - {shortCode}")

    if not shlink.is_valid(shortCode):
        print("BROKEN LINK!!")
    
    # shlink.delete_link(shortCode)
    #shlink.add_link(link['title'], link['longUrl'], shortCode, link['tags'])