import pytest


@pytest.mark.parametrize("name_or_id, name, response_code", [
    ("ditto", "ditto", 200),
    (1, "bulbasaur", 200),
    (-1, None, 404),
    ("fake_pokemon", None, 404),
])
def test_get_pokemon_by_id_or_name(pokeapi, name_or_id, name, response_code):
    response = pokeapi.pokemon.get_pokemon(name_or_id)
    assert response.status_code == response_code, f"Expected status code 200, but got {response.status_code}"
    if response_code == 200:
        json_response = response.json()
        assert json_response["name"] == name


@pytest.mark.parametrize("pokemon_id, expected_stats", [
    (1, {"hp", "attack", "defense", "special-attack", "special-defense", "speed"}),
])
def test_pokemon_has_base_stats(pokeapi, pokemon_id, expected_stats):
    response = pokeapi.pokemon.get_pokemon(pokemon_id)
    json_response = response.json()
    assert "stats" in json_response, "Response does not contain the 'stats' key"
    stats = json_response["stats"]

    stats_names = {stat["stat"]["name"] for stat in stats}
    assert stats_names == expected_stats
    for stat in stats:
        name = stat["stat"]["name"]
        value = stat.get("base_stat")
        assert isinstance(value, int) and value > 0, f"{name} base_stat is invalid: {value}"
