#Для практики также реализован варинт с тестированием сценария в структуре одного теста. Основным решением является test_pet_lifecycle_one_test.py

def test_life_cycle_pet(session_pet_client, example_pet_data, for_update_pet_data):
    create_pet = session_pet_client.create_pet(example_pet_data)
    assert create_pet.status_code == 200
    assert create_pet.json().get('id') == example_pet_data['id']

    created_pet = session_pet_client.get_pet(example_pet_data['id'])
    assert created_pet.status_code == 200
    assert created_pet.json().get("name") == example_pet_data["name"]
    assert created_pet.json().get("status") == example_pet_data["status"]

    update_pet = session_pet_client.update_pet(for_update_pet_data)
    assert update_pet.status_code == 200

    updated_pet = session_pet_client.get_pet(example_pet_data['id'])
    assert updated_pet.status_code == 200
    assert updated_pet.json().get('name') == for_update_pet_data['name']
    assert not updated_pet.json().get('status') #фактическая реализация, еслм в запросе обновления не был указан статус, поле удаляется

    delete_pet = session_pet_client.delete_pet(example_pet_data['id'])
    assert delete_pet.status_code == 200

    deleted_pet = session_pet_client.get_pet(example_pet_data['id'])
    assert deleted_pet.status_code == 404