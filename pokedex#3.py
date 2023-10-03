import requests
import sys
import re



# sample data = bulbasaur ivysaur venusaur charmander charmeleon charizard     
        
def input_pokemon_names():
     names = input("Enter Pokemon names separated by space: ")
     
     return re.split('\s', names)
     
        
def search_pokemon(pokemon_names):
        for name in pokemon_names:
        
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/") 
            
            if response.status_code == 200:
                pokemon_data = response.json()
                
                pokemon_name = pokemon_data["name"] 
                pokemon_hp = pokemon_data["base_experience"] 
                pokemon_attacks = [item['move']['name'] for item in pokemon_data['moves']]
                pokemon_held_items = [item['item']['name'] for item in pokemon_data['held_items']]
                
                print('----------------------------------------------------------------------------------------------------------------------------------------')

                print(f"Name: {pokemon_name.capitalize()}")
                print(f"HP: {pokemon_hp}/{pokemon_hp}")
                print(f"Attacks: {', '.join(pokemon_attacks)}")
                print(f"Held Items: {', '.join(pokemon_held_items)}")
                
                print('----------------------------------------------------------------------------------------------------------------------------------------')


                
                
            else:
                print(f"{name} doesn't exist")
                
            
              
        
if __name__ == "__main__":
    
    if len(sys.argv) == 1 :
        pokemon_names = input_pokemon_names()
    else:
        pokemon_names = sys.argv[1:]
        
    search_pokemon(pokemon_names)
    

