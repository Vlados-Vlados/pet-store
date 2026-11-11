import requests

URL_BASE = "https://petstore.swagger.io/v2"
URL_PET_PATH = URL_BASE + "/pet"
AUTH_PATH = "/oauth/authorize"

#Настраивал прокси(Charles) для более подробного и удобного просмотра отправленного питоном запроса.
#Просто хочу это оставить в одном из проектов, чтобы если понадобится, была возможность быстро вспомнить реализацию. И как напоминание.
USE_PROXY = False
PROXIES = {
    "http": "127.0.0.1:8888",
    "https": "127.0.0.1:8888"
}
CERT_PATH = "/usr/local/share/ca-certificates/charles-5.2.2.crt" #Путь к сертификату Charles на Linux

class PetClient:
    def __init__(self):
        self.session = requests.Session()

    def create_pet(self, payload):
        if not USE_PROXY:
            r = self.session.post(url=URL_PET_PATH, json=payload, timeout=5)
        else:
            r = self.session.post(url=URL_PET_PATH, proxies=PROXIES, verify=CERT_PATH, json=payload, timeout=5)

        return r

    def get_pet(self, pet_id):
        get_pet_url = URL_PET_PATH + f"/{pet_id}"
        r = self.session.get(url=get_pet_url, timeout=5)

        return r

    def update_pet(self, payload):
        r = self.session.put(url=URL_PET_PATH, json=payload, timeout=5)

        return r

    def delete_pet(self, pet_id):
        get_pet_url = URL_PET_PATH + f"/{pet_id}"
        r = self.session.delete(url=get_pet_url, timeout=5)

        return r