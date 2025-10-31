from api.pagination import Pagination
from api.pokemon import Pokemon

"""
Represents the entry point for working with PokeApi
"""


class PokeApi:
    pokemon: Pokemon
    pagination: Pagination

    def __init__(self, api_client):
        self.pokemon = Pokemon(api_client)
        self.pagination = Pagination(api_client)
