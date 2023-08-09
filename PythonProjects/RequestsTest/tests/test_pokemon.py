import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = 'dfbe4a1dbe69b89336eddf41c459b389'

def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 1971})
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 1971})
    assert response.json()['trainer_name'] == 'AlexN'
