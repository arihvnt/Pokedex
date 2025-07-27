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
    height = data["height"] / 10  #Convert decimetres to metres
    weight = data["weight"] / 10      #Convert hectograms to kilograms
    sprites=data["sprites"]["front_default"]

    #species data for flavor text, region, generation and evolution
    species_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon.lower()}"
    species_data = requests.get(species_url).json()

    #flavor text
    flavor_text = next(
        (entry['flavor_text'].replace('\n', ' ').replace('\f', ' ') for entry in species_data['flavor_text_entries'] if entry['language']['name'] == 'en'),
        "No flavor text available."
    )

    #generation and region
    generation = species_data["generation"]["name"].replace("generation-", " ").upper()
    generation_to_region = {
    "generation-i": "Kanto",
    "generation-ii": "Johto",
    "generation-iii": "Hoenn",
    "generation-iv": "Sinnoh",
    "generation-v": "Unova",
    "generation-vi": "Kalos",
    "generation-vii": "Alola",
    "generation-viii": "Galar",
    "generation-ix": "Paldea"
}
    region = generation_to_region.get(generation, "unknown")

    #evolution data
    evolves_from = species_data["evolves_from_species"]
    if evolves_from: 
        evolves_from = evolves_from["name"].capitalize()
    else: 
        evolves_from = "None"



    print(f"\n POKEMON INFO - {name}")
    print(f"Type(s): {'. '.join(types)}")
    print(f"Abilities: {'. '.join(abilities)}")
    print("Bae Stats: ")
    for stat, value in stats.items():
        print(f"   - {stat.capitalize()}: {value}")
    print(f"\n Height: {height}m  Weight: {weight}kg")
    print(f"\n Generation: {generation}")

    gen_key = species_data["generation"]["name"]
    region = generation_to_region.get(gen_key, "unknown")
    print(f"\n Region: {region}")
    
    print(f"\n Evolves from: {evolves_from}")
    print(f"\n Description: {flavor_text}")
    print(f"Sprite URL: {sprites}")

if __name__ == "__main__":
    while True:
        pokemon = input("Enter the name or ID of the Pokémon: ").lower().strip()
        try:
            get_pokemon_data(pokemon)
            break  # Exit loop if successful
        except:
            print("Error: Pokémon not found. Check if you've written the spelling/ID correctly.\n")