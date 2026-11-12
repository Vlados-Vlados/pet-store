"""
Выбрана структура нескольких тестов для проверки сценария, чтобы сразу видеть какой именно шаг падает, а какие остаются на плаву.
Локализация удобнее и читаемость шагов лучше.
При этом объединив тесты в класс , который логически связывает их как жизненный цикл,
нет проблем с тем чтобы в отчете понимать и легко видеть что эти отдельные тесты относятся именно к общему сценарию.
Но и в то же время сохраняется возможность в ручную проверить лишь часть сценария.
И, наверное, сохраняется удобство переиспользования при необходимости.
"""

class TestPetLifecycle:
    def test_create_pet(self, create_pet):
        assert create_pet.status_code == 200
        assert create_pet.json()

    def test_read_after_created_pet(self, get_created_pet, example_pet_data):
        assert get_created_pet.status_code == 200
        assert get_created_pet.json()["name"] == example_pet_data["name"]
        assert get_created_pet.json()["status"] == example_pet_data["status"]

    def test_update_created_pet(self, update_pet):
        assert update_pet.status_code == 200

    def test_read_after_updating_pet(self, get_created_pet, for_update_pet_data, example_pet_data):
        assert get_created_pet.status_code == 200
        assert get_created_pet.json()['name'] == for_update_pet_data['name']
        assert not get_created_pet.json().get('status') #фактическая реализация, еслм в запросе обновления не был указан статус, поле удаляется

    def test_delete_exist_pet(self, delete_pet):
        assert delete_pet.status_code == 200

    def test_read_after_deleting_pet(self, get_created_pet):
        assert get_created_pet.status_code == 404