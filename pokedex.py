import requests
import sys

def search_pokemon(name):

        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/") 
        pokemon = response.json()
        
        print(f'Name: {pokemon["name"].capitalize()}')     
        print(f'ID: {pokemon["id"]}')
        print(f'Base XP: {pokemon["base_experience"]}')
        

if __name__ == "__main__":
    search_pokemon(sys.argv[1])