"""
Represents 'Pokemon' group in PokeApi
"""
from requests import Response

from api import endpoints


class Pokemon:
    def __init__(self, api_client):
        self.client = api_client

    def get_pokemon(self, name_or_id: str | int) -> Response:
        return self.client.get(f"{endpoints.POKEMON}/{name_or_id}")
