import requests


class MyIP():    

    url = "https://api.ipify.org/?format=json"

    def get_my_ip(self) -> str:
        '''Возвращает мой IP-адрес'''

        response = requests.get(MyIP.url)
        response.raise_for_status()
        result = response.json()["ip"]
        return result
    

class IPInfo():

    base_url = "https://ipinfo.io/"
    path = "geo"

    def get_ip_info(self, ip: str) -> dict:
        '''Возвращает информацию по IP'''

        url = f"{IPInfo.base_url}/{ip}/{IPInfo.path}"
        response = requests.get(url)
        response.raise_for_status()
        result = response.json()
        return result
    

if __name__ == "__main__":

    ip = MyIP()
    print(ip.get_my_ip())
    ip_info = IPInfo()
    print(ip_info.get_ip_info(ip.get_my_ip()))
