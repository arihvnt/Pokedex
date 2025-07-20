import requests
def get_pokemon_data(pokemon):
    url=f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
    response=requests.get(url)
    
    if response.status_code != 200:
        print(f"error: pokemon not found. check if you've written the spelling/ID correctly")
        return 
    
    data=response.json()
    
    name=data["name"].capitalize()
    types=[t["type"]["name"] for t in data["types"]]
    abilities=[a["ability"]["name"] for a in data["abilities"]]
    stats={s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
    sprites=data["sprites"]["front_default"]

    print(f"\n POKEMON INFO - {name}")
    print(f"Type(s): {'. '.join(types)}")
    print(f"Abilities: {'. '.join(abilities)}")
    print("Bae Stats: ")
    for stat, value in stats.items():
        print(f"   - {stat.capitalize()}: {value}")
    print(f"Sprite URL: {sprites}")

if __name__ == "__main__":
    pokemon=input("enter the name or ID of the pokemon:")
    get_pokemon_data(pokemon)