# 🧿 Pokédex CLI — Python x PokéAPI

A simple command-line based Pokédex built using Python and the [PokéAPI](https://pokeapi.co/).  
Type a Pokémon's name or ID and get all its details with just a press of a button.

---

## Version

**v1.5 – July 2025**

New in this version:
- Added flavor text (official Pokédex description)
- Shows generation and region
- Shows what the Pokémon evolves **from**
- Improved user input and error handling (asks again if Pokémon is not found)
- Cleaner formatting of height, weight, and stats

---

Features: 

- Search Pokémon by name or ID
- Displays type(s), stats, height, weight
- Pulls live data using `requests` and PokéAPI
- Prints image link (sprite) for visual use

---

Building Blocks

- Python
- [Requests](https://pypi.org/project/requests/)
- [PokéAPI](https://pokeapi.co/)

---

## Screenshots

### 🔹 Terminal Output
![Code Output](assets/code.png)

### 🔹 Program Running
![Program Screenshot](assets/program.png)

---

Installation Procedure

```bash
git clone https://github.com/arihvnt/Pokedex.git
cd Pokedex
pip install -r requirements.txt