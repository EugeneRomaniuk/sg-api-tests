# PokeAPI Test Suite

This project contains a suite of automated API tests for the public [PokéAPI](https://pokeapi.co/). It uses Python with
the `pytest` and `requests` libraries to validate the functionality and data integrity of the Pokémon API endpoint.

## Setup and Installation

1. **Clone repository and navigate to project root**

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

To execute the test suite, run the following command from the project's root directory:

```bash
pytest
```

## Test Cases

The following test cases are implemented to validate the `/pokemon` endpoint.

### `test_get_pokemon_by_id_or_name`

| Test Case Description | Input (`name_or_id`) | Expected Status Code | Expected Name |
| :-------------------- | :------------------- | :------------------- | :------------ |
| Get Pokémon by valid name | `"ditto"` | 200 | `"ditto"` |
| Get Pokémon by valid ID (1) | `1` | 200 | `"bulbasaur"` |
| Get Pokémon by invalid ID (-1) | `-1` | 404 | N/A |
| Get Pokémon by invalid name | `"fake_pokemon"` | 404 | N/A |

### `test_pokemon_has_base_stats`

| Test Case Description | Input (`pokemon_id`) | Expected Stats |
| :-------------------- | :------------------- | :------------------------------------------------------------------------- |
| Validate base stats for Bulbasaur | `1` | `{"hp", "attack", "defense", "special-attack", "special-defense", "speed"}` |

### `test_pokemon_list_pagination`

These tests validate the pagination functionality of the `/pokemon` resource list endpoint using the `limit` and
`offset` query parameters.

| Test Case Description                  | Input (`limit`, `offset`) | Expected Result Count | First Pokemon Name |
|:---------------------------------------| :------------------------ | :------------------- | :-------------------- |
| Get default list of Pokémon            | `None`, `None` | 20 | `bulbasaur` |
| Get list with limit 0 (defaults to 20) | `0`, `0` | 20 | `bulbasaur` |
| Get list with lower limit and offset   | `9`, `10` | 9 | `metapod` |
| Get list with higher limit and offset  | `21`, `10` | 21 | `metapod` |
| Get the last item in the list          | `None`, `1327` | 1 | `falinks-mega` |
| Get list with offset beyond total      | `None`, `1328` | 0 | None |
