import requests
<<<<<<< HEAD
from difflib import get_close_matches
from colorama import Fore, Style, init

# initialize colorama
init(autoreset=True)

# ------------------ FETCH DATA ------------------
def fetch_pokemon(name_or_id):
    """Fetch Pokémon details from PokéAPI"""
    url = f"https://pokeapi.co/api/v2/pokemon/{name_or_id.lower()}"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    species_url = f"https://pokeapi.co/api/v2/pokemon-species/{name_or_id.lower()}"
    species_data = requests.get(species_url).json()

    # flavor text
    flavor_text = next(
        (entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
         for entry in species_data['flavor_text_entries']
         if entry['language']['name'] == 'en'),
        "No flavor text available."
    )

    # generation → region mapping
    gen_key = species_data["generation"]["name"]
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

    # evolution
    evolves_from = species_data["evolves_from_species"]
    evolves_from = evolves_from["name"].capitalize() if evolves_from else "None"

    return {
        "name": data["name"].capitalize(),
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
        "height": data["height"] / 10,
        "weight": data["weight"] / 10,
        "sprite": data["sprites"]["front_default"],
        "flavor_text": flavor_text,
        "generation": gen_key.upper().replace("GENERATION-", ""),
        "region": generation_to_region.get(gen_key, "Unknown"),
        "evolves_from": evolves_from
    }

# ------------------ DISPLAY INFO ------------------
def show_pokemon_info(pokemon):
    """Print Pokémon details in a formatted way"""
    data = fetch_pokemon(pokemon)
    if not data:
        print(Fore.RED + f"Error: Pokémon '{pokemon}' not found.")
        return

    print(Fore.CYAN + f"\n=== {data['name']} ===" + Style.RESET_ALL)
    print("Types:", ", ".join(data["types"]))
    print("Abilities:", ", ".join(data["abilities"]))
    print("\nBase Stats:")
    for stat, value in data["stats"].items():
        print(f"  - {stat.capitalize()}: {value}")
    print(f"\nHeight: {data['height']} m   Weight: {data['weight']} kg")
    print(f"Generation: {data['generation']}   Region: {data['region']}")
    print(f"Evolves from: {data['evolves_from']}")
    print("\nPokédex Entry:", data["flavor_text"])
    print("Sprite:", data["sprite"])

# ------------------ COMPARE TOOL ------------------
def compare_pokemon(p1, p2):
    """Compare two Pokémon stats side by side"""
    data1 = fetch_pokemon(p1)
    data2 = fetch_pokemon(p2)

    if not data1 or not data2:
        print(Fore.RED + "Error fetching one or both Pokémon.")
        return

    print(Fore.YELLOW + f"\n🔹 Comparing {data1['name']} vs {data2['name']} 🔹")
    for stat in data1["stats"]:
        s1 = data1["stats"][stat]
        s2 = data2["stats"][stat]
        better = data1['name'] if s1 > s2 else (data2['name'] if s2 > s1 else "Equal")
        print(f"{stat.capitalize():<12}: {s1} vs {s2} → {better}")

# ------------------ FUZZY SEARCH ------------------
def get_pokemon_list():
    """Fetch all Pokémon names once (for fuzzy search)"""
    url = "https://pokeapi.co/api/v2/pokemon?limit=10000"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    data = response.json()
    return [p["name"] for p in data["results"]]

ALL_POKEMON = get_pokemon_list()

def fuzzy_search(query):
    """Suggest close matches for misspelled Pokémon names"""
    return get_close_matches(query.lower(), ALL_POKEMON, n=3, cutoff=0.6)

# ------------------ MAIN MENU ------------------
def main():
    while True:
        print(Fore.GREEN + "\nMain Menu:")
        print("1. Search Pokémon")
        print("2. Compare two Pokémon")
        print("3. Exit")
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            query = input("\nEnter Pokémon name or ID: ").strip().lower()
            if query == "exit":
                continue

            data = fetch_pokemon(query)
            if not data:
                suggestions = fuzzy_search(query)
                if suggestions:
                    print(Fore.YELLOW + "\nDid you mean:")
                    for i, s in enumerate(suggestions, 1):
                        print(f"  {i}. {s.title()}")
                    choice = input("Choose a number (or press Enter to skip): ").strip()
                    if choice.isdigit():
                        choice = int(choice)
                        if 1 <= choice <= len(suggestions):
                            show_pokemon_info(suggestions[choice - 1])
                            continue
                print(Fore.RED + "Pokémon not found.")
            else:
                show_pokemon_info(query)

        elif choice == "2":
            p1 = input("First Pokémon: ").strip()
            p2 = input("Second Pokémon: ").strip()
            compare_pokemon(p1, p2)

        elif choice == "3":
            print(Fore.CYAN + "Exiting Pokédex. Goodbye!")
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again.")

# ------------------ RUN ------------------
if __name__ == "__main__":
    main()
=======
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
>>>>>>> da979286c4c90425b3714309751cf6e6adba7dd9
