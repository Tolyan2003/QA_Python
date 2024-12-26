import requests
from settings  import LOGIN, PASSWORD, BASE_URL, COMPANY_ID, USER_KEY

class You_Gile:
    def __init__(self):
        self.login = LOGIN
        self.password = PASSWORD
        self.company_id = COMPANY_ID
        self.url = BASE_URL
        self.id = USER_KEY

    # Получаем ID компании
    def get_comp(self):
        payload = {
            "login": self.login,
            "password": self.password,
            'name': 'My_Comp_LAA'
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(
            f"{self.url}auth/companies", json=payload, headers=headers
        )
        response.raise_for_status()
        return response.json()

    def get_auth_key(self, company_id):
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": self.company_id,
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(
            f"{self.url}auth/keys", json=payload, headers=headers
        )
        response.raise_for_status()
        return response.json()

    def get_keys_comp(self):
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": self.company_id,
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(
            f"{self.url}auth/keys/get", json=payload, headers=headers
        )
        response.raise_for_status()
        return response.json()

    # Список сотрудников
    def list_staffer(self):
        headers = {
            'Authorization': 'Bearer ' + USER_KEY,
            'Content-Type': 'application/json'
        }
        response = requests.get(f"{self.url}users",
                                  headers=headers
                                  )
        response.raise_for_status()
        return response.json()

    def add_staffer(self):
        headers = {
            'Authorization': 'Bearer ' + USER_KEY,
            'Content-Type': 'application/json'
        }
        payload = {
            "email": "ttl2003.al@gmail.ru"
        }
        response = requests.post(f"{self.url}users",
                                 json=payload,
                                 headers=headers
                                  )
        response.raise_for_status()
        return response.json()

    # [POST] добавление проекта
    def add_project(self, name_project):
        headers = {
            'Authorization': 'Bearer ' + USER_KEY,
            'Content-Type': 'application/json'
        }
        payload = {
            "title": name_project,
            "users": {
                'd21d9f2a-e7c4-43b2-a540-06a565b9d9c5': 'admin',
                '01b2ac97-bc61-4c60-b745-ee0d019ab472': 'worker'
            }
        }
        response = requests.post(f"{self.url}projects",
                                 json=payload,
                                 headers=headers
                                  )
        response.raise_for_status()
        return response.json()

    # Негативный тест
    def add_project_N(self):
        headers = {
            'Authorization': 'Bearer ' + USER_KEY,
            'Content-Type': 'application/json'
        }
        payload = {
            "title": "ГроссБух",
            "users": {
                'd21d9f2a-e7c4-43b2-a540-06a565b9d9c5': '',
                '01b2ac97-bc61-4c60-b745-ee0d019ab472': ''
            }
        }
        response = requests.post(f"{self.url}projects",
                                 json=payload,
                                 headers=headers
                                 )
        assert response.status_code == 400
        return response.json()

    # [GET] список проектов
    def list_project(self):
        headers = {
            'Authorization': 'Bearer ' + USER_KEY,
            'Content-Type': 'application/json'
        }
        response = requests.get(f"{self.url}projects",
                                 headers=headers
                                  )
        response.raise_for_status()
        return response.json()

    # негативный тест
    def list_project_neg(self):
        headers = {
            'Authorization': USER_KEY,
            'Content-Type': 'application/json'
        }
        response = requests.get(f"{self.url}projects",
                                 headers=headers
                                  )
        assert response.status_code == 401
        return response.json()

    # [PUT] /api-v2/projects/{id}
    def put_project(self, name_project):
        headers = {
            'Authorization': 'Bearer ' + USER_KEY,
            'Content-Type': 'application/json'
        }
        payload = {
            "title": name_project,
            "users": {
                'd21d9f2a-e7c4-43b2-a540-06a565b9d9c5': 'admin',
                '01b2ac97-bc61-4c60-b745-ee0d019ab472': 'worker'
            }
        }
        response = requests.put(f"{self.url}projects/b0e0c73f-9123-4340-bb55-f05f21400fcc",
                                 json=payload,
                                 headers=headers
                                  )
        response.raise_for_status()
        return response.json()

    # негативный тест
    def put_project_neg(self):
        headers = {
            'Authorization': 'Bearer ' + USER_KEY,
            'Content-Type': 'application/json'
        }
        payload = {
            # "title": name_project,
            "users": {
                'd21d9f2a-e7c4-43b2-a540-06a565b9d9c5': 'admin',
                '01b2ac97-bc61-4c60-b745-ee0d019ab472': 'worker'
            }
        }
        response = requests.put(f"{self.url}projects",
                                 json=payload,
                                 headers=headers
                                  )
        assert response.status_code == 404
        return response.json()

    # [GET] /api-v2/projects/{id}
    def get_project_id(self):
        headers = {
            'Authorization': 'Bearer ' + USER_KEY,
            'Content-Type': 'application/json'
        }
        response = requests.get(f"{self.url}projects/b0e0c73f-9123-4340-bb55-f05f21400fcc",
                                 headers=headers
                                  )
        response.raise_for_status()
        return response.json()

    # негативный тест
    def get_project_id_neg(self):
        headers = {
            'Authorization': '',
            'Content-Type': ''
        }
        response = requests.get(f"{self.url}projects/b0e0c73f-9123-4340-bb55-f05f21400fcc",
                                 headers=headers
                                  )
        assert response.status_code == 401
        return response.json()