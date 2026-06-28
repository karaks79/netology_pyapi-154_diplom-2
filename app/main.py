from app import MyIP, IPInfo, YandexDiskAPI 
from app.config import YANDEX_DISK_TOKEN


if __name__ == "__main__":
    
    # Мой IP
    ip_obj = MyIP()
    ip = ip_obj.get_my_ip()
    #print(ip)

    # Инфо по IP
    ip_info_obj = IPInfo()
    ip_info = ip_info_obj.get_ip_info(ip)
    #print(ip_info)
    #print(f"{type(ip_info)=}")

    # Загрузка на Яндекс.Диск
    yandex_disk_api = YandexDiskAPI(YANDEX_DISK_TOKEN)
    yandex_disk_api.load_to_yandex_disk(ip_info)
        

    