import requests
import sys

def search_pokemon(name):

        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/") 
        
        
        if response.status_code == 200:
            pokemon = response.json()
            print(f'Name: {pokemon["name"].capitalize()}')     
            print(f'ID: {pokemon["id"]}')
            print(f'Base XP: {pokemon["base_experience"]}')
            
        else:
            print(f"'{name}' does not exist")
        
        
def input_pokemon_name():
    return str(input("Enter name of Pokemon: "))
        

if __name__ == "__main__":
    
    if len(sys.argv) == 1 :
        pokemon_name = input_pokemon_name()
    else:
        pokemon_name = sys.argv[1]
        
    search_pokemon(pokemon_name)