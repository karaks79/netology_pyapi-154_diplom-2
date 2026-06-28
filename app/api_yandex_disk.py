import json
import requests
from app.config import YANDEX_DISK_TOKEN

class YandexDiskAPI():
  
    base_url = "https://cloud-api.yandex.net"
    disk_resources = "v1/disk/resources"
    folder = "netology_pyapi-154"


    def __init__(self, token: str):
        self.token = token


    def is_folder_exists(self) -> bool:
        '''Проверяет - есть ли папка folder на Яндекс.Диске'''

        response = requests.get(
            url=f"{self.base_url}/{self.disk_resources}",
            params={"path": f"disk:/{self.folder}"},
            headers={"Authorization": f"OAuth {self.token}"}
        )

        if response.status_code == 200:
            return True
        
        if response.status_code == 404:
            return False
        
        response.raise_for_status()

    
    def create_folder(self):
        '''Создает папку folder'''

        response = requests.put(
            url=f"{self.base_url}/{self.disk_resources}",
            params={"path": f"disk:/{self.folder}"},
            headers={"Authorization": f"OAuth {self.token}"}
        )
        response.raise_for_status()

        return response.status_code < 300


    def delete_folder(self):
        '''Удаляет папку folder'''

        response = requests.delete(
            url=f"{self.base_url}/{self.disk_resources}",
            params={"path": f"disk:/{self.folder}"},
            headers={"Authorization": f"OAuth {self.token}"}
        )
        response.raise_for_status()

        return response.status_code < 300


    def load_to_yandex_disk(self, ip_info: dict):
        '''
            Преобразует словарь в JSON.
            Создает на Яндекс.Диск папку folder, если её там нет.
            Загружает JSON на Яндекс.Диск в папку folder. 
        '''
        
        # Преобразовать словарь в JSON
        ip_info_json = json.dumps(ip_info, ensure_ascii=False, indent=4)

        # Создать на Яндекс.Диск папку folder, если её там нет
        if not self.is_folder_exists():
            self.create_folder()

        # Получить ссылку для загрузки файла на Диск по пути path. 
        response_get = requests.get(
            url = f"{self.base_url}/{self.disk_resources}/upload",
            params={
                "path": f"disk:/{self.folder}/data.json",
                "overwrite": "true"
            },
            headers={"Authorization": f"OAuth {self.token}"}
        )
        response_get.raise_for_status()
        href = response_get.json()["href"]

        # Загрузить JSON на Яндекс.Диск в папку folder. 
        response_put = requests.put(url=href, data=ip_info_json)
        response_put.raise_for_status()

    
if __name__ == "__main__":

    yandex_disk_api = YandexDiskAPI(YANDEX_DISK_TOKEN)
    
    print(yandex_disk_api.is_folder_exists())
    if not yandex_disk_api.is_folder_exists():
        print(f"{yandex_disk_api.create_folder()=}")
    else:
        print(f"{yandex_disk_api.delete_folder()=}")