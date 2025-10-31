import pytest

from api.api_client import ApiClient
from api.poke_api import PokeApi


@pytest.fixture(scope="session")
def api_client() -> ApiClient:
    return ApiClient(base_url="https://pokeapi.co/api/v2")


@pytest.fixture(scope="session")
def pokeapi(api_client) -> PokeApi:
    return PokeApi(api_client)
