import requests
import pprint
url = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(url)
pprint.pprint(response.json())

