import requests


response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json ={
    "name": "generate",
    "photo": "generate"
},headers = {'Content-Type':'application/json','trainer_token':'dfbe4a1dbe69b89336eddf41c459b389'})
print(response.text)

response_change_name = requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {"pokemon_id": "6027",
    "name": "pikachu","photo": "https://dolnikov.ru/pokemons/albums/025.png"},headers = {'Content-Type':'application/json','trainer_token':'dfbe4a1dbe69b89336eddf41c459b389'})
print(response_change_name.text)

response_pokeball = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball',json = {
    "pokemon_id": "6027"},headers = {'Content-Type':'application/json','trainer_token':'dfbe4a1dbe69b89336eddf41c459b389'})
print(response_pokeball.text)
