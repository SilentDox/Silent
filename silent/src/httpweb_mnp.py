import requests
from .config import COLOR_CODE, console_clear
from functools import lru_cache


# Проверка по MNP
class HttpWebMnp:
    """Информация получаемая с сайта httpweb.ru никак\n
    не синхронизирован/связан с silent а так-же с sil3nt.
    :param: `user_number` - Номер телефона."""

    def __init__(self) -> None:
        self.__check_mnp_link: str = "https://htmlweb.ru/json/mnp/phone/"
        self.__not_found_text: str = "Информация отсутствует"

    # Получение данных MNP по номеру
    @lru_cache(maxsize=None)
    def __get_mnp_data(self, user_number: str) -> dict:
        """Получение данных MNP по номеру
        param: `self.__check_mnp_link:` str — Адрес сайта для получения MNP данных по номеру.
        return: `__return_mnp_data:` dict - MNP Данные клиента.
        """

        # Получение данных MNP по номеру тел. клиента 
        try:
            __result_mnp_data = requests.get(self.__check_mnp_link + user_number)
        
            if __result_mnp_data.ok:
                __get_mnp_data = __result_mnp_data.json()
            
            else:
                __get_mnp_data = {"status_error": True}

        except requests.exceptions.ConnectionError as connection_error:
            __get_mnp_data = {"status_error": True}
        
        return __get_mnp_data

    # Ввод данных в консоль
    @property
    def print_mnp_results(self) -> str:
        """Вывод полученных данных"""

        try:
            console_clear()
            _user_number: str = input(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}2{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}' + 
                f'Введите номер телефона: {COLOR_CODE["RED"]}').strip()
            
            # Если ввели номер телефона
            if _user_number:
                print(f'{COLOR_CODE["RED"]}[~] {COLOR_CODE["RED"]}Поиск данных.. {COLOR_CODE["RED"]}\n')
                _get_user_mnp_data = self.__get_mnp_data(user_number=_user_number)
                
                # Проверка статуса ошибки
                if _get_user_mnp_data.get("limit") <= 0:
                    print(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[!] '+
                        f'{COLOR_CODE["RED"]}К сожалению, вы израсходовали {COLOR_CODE["DARK"]}все лимиты')
                    
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Всего лимитов: {COLOR_CODE["DARK"]}'+
                        f'{str(_get_user_mnp_data.get("limit", self.__not_found_text))}{COLOR_CODE["RED"]}')
                
                # Проверка статуса ошибки
                elif _get_user_mnp_data.get("status_error") or _get_user_mnp_data.get("error"):
                    print(f'{COLOR_CODE["RED"]}[!] {COLOR_CODE["RED"]}Данные не найдены {COLOR_CODE["RED"]}\n')

                # Ввод данных о номере
                else:
                    _mnp_data_city = str(_get_user_mnp_data.get('city', self.__not_found_text)).replace("0", self.__not_found_text)
                    _mnp_data_region = _get_user_mnp_data.get('region')
                    _mnp_data_operator = _get_user_mnp_data.get('oper')
                    

                    # Код страны            
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Код страны:{COLOR_CODE["RED"]} '+
                        f'{str(_mnp_data_region.get("country", self.__not_found_text))}{COLOR_CODE["RED"]}')

                    # Город
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Город регистрации:{COLOR_CODE["RED"]} '+
                        f'{_mnp_data_city}{COLOR_CODE["RED"]}')

                    # Оператор
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Оператор:{COLOR_CODE["RED"]} '+
                        f'{_mnp_data_operator.get("brand", self.__not_found_text)}{COLOR_CODE["DARK"]} '+
                            f'({_mnp_data_operator.get("name", self.__not_found_text)}, '+
                            f'{_mnp_data_operator.get("url", self.__not_found_text)}){COLOR_CODE["RED"]}')

                    # Местоположение
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Местоположение:{COLOR_CODE["RED"]} '+
                        f'{_mnp_data_region.get("name", self.__not_found_text)}{COLOR_CODE["DARK"]} '+
                        f'({_mnp_data_region.get("okrug", self.__not_found_text)}){COLOR_CODE["RED"]}')

                    # Автомобильные коды
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Автомобильные коды:{COLOR_CODE["RED"]} '+
                        f'{_mnp_data_region.get("autocod", self.__not_found_text)}{COLOR_CODE["RED"]}')

                    # Об операторе
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Об операторе:{COLOR_CODE["RED"]} '+
                        f'{_mnp_data_region.get("wiki", self.__not_found_text)}{COLOR_CODE["RED"]}')
            
                    # Всего лимитов
                    print(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Всего лимитов: '+
                        f'{str(_get_user_mnp_data.get("limit", self.__not_found_text))}{COLOR_CODE["RED"]}')

                    input(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}' + 
                        f'Чтобы завершить поиск, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RED"]}ENTER ')

            # Если не ввели номер телефона
            else:
                print(f'{COLOR_CODE["RED"]}[!] {COLOR_CODE["RED"]}Ошибка, введите номер телефона! {COLOR_CODE["RED"]}\n')

        except KeyboardInterrupt:
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["RED"]}Вынужденная остановка работы! {COLOR_CODE["RED"]}\n')

