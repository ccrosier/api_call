import requests
import pprint

pokemon = input("Enter name of pokemon: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

try:
    response = requests.get(url)
    pprint.pprint(response.json(), compact=True)
except:
    print(f"Error making API call to: {url}\n\t{response}")

