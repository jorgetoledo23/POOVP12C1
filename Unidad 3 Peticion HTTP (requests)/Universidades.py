import requests

r = requests.get("http://universities.hipolabs.com/search?country=United+States")

data = r.json()

for a in data:
    Universidad = a
    print(Universidad['name'])
    print(Universidad['web_pages'][0])
    print("")