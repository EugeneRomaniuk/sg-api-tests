import pytest

from api import endpoints

"""
Calling any API endpoint without a resource ID or name will return a paginated list of available resources for that API.
 By default, a list "page" will contain up to 20 resources. If you would like to change this just add a 'limit' 
 query parameter to the GET request, e.g. ?limit=60. You can use 'offset' to move to the next page,
 e.g. ?limit=60&offset=60.
"""

POKEMON_COUNT = 1328


@pytest.mark.parametrize("limit, offset, expected_count, first_pokemon_name", [
    (None, None, 20, "bulbasaur"),
    (0, 0, 20, "bulbasaur"),
    (9, 10, 9, "metapod"),
    (21, 10, 21, "metapod"),
    (None, POKEMON_COUNT - 1, 1, "falinks-mega"),
    (None, POKEMON_COUNT, 0, None),
])
def test_get_pokemon_list_with_pagination(pokeapi, limit, offset, expected_count, first_pokemon_name):
    response = pokeapi.pagination.get_resource_list(endpoints.POKEMON, limit, offset)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    json_response = response.json()
    assert "results" in json_response, "Response does not contain the 'results' key"

    results = json_response["results"]
    actual_count = len(results)
    assert actual_count == expected_count, f"Expected {expected_count} Pokémon, but got {actual_count}"

    if expected_count > 0:
        actual_name = results[0]["name"]
        assert actual_name == first_pokemon_name, (
            f"Expected the first Pokémon's name to be '{first_pokemon_name}', but got '{actual_name}'"
        )
