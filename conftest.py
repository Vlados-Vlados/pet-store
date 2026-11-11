import pytest
from api.api_client import PetClient

pet_client = None

@pytest.fixture(scope="session")
def session_pet_client(example_pet_data):
    pet_client = PetClient()

    yield pet_client
    pet_client.delete_pet(example_pet_data['id'])


@pytest.fixture
def create_pet(example_pet_data, session_pet_client):
    r = session_pet_client.create_pet(example_pet_data)

    return r

@pytest.fixture
def get_created_pet(example_pet_data, session_pet_client):
    r = session_pet_client.get_pet(example_pet_data["id"])

    return r

@pytest.fixture
def update_pet(for_update_pet_data, session_pet_client):
    r = session_pet_client.update_pet(for_update_pet_data)

    return r

@pytest.fixture
def delete_pet(for_update_pet_data, session_pet_client):
    r = session_pet_client.delete_pet(for_update_pet_data['id'])

    return r

@pytest.fixture(scope="session")
def example_pet_data():
    """Данные создаваемго животного"""
    new_pet = {
        "id": 9456435345,
        "name": "Kesha",
        "status": "was born"
    }

    return new_pet

@pytest.fixture(scope="session")
def for_update_pet_data():
    """Данные создаваемго животного"""
    update_pet = {
        "id": 9456435345,
        "name": "Zeus"
    }

    return update_pet