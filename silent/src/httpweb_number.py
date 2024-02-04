import requests
from .config import COLOR_CODE, console_clear
from .phoneradar_ru import PhoneRadar
from functools import lru_cache

class HttpWebNumber:
    """Информация получаемая с сайта httpweb.ru никак\n
    не синхронизирован/связан с silent а так-же с sil3nt.
    :param: `user_number` - Номер телефона."""
    
    def __init__(self) -> None:
        self.__check_number_link: str = "https://htmlweb.ru/geo/api.php?json&telcod="
        self.__not_found_text: str = "Информация отсутствует"

    # Получение данных по номеру
    @lru_cache(maxsize=None)
    def __return_number_data(self, user_number: str) -> dict:
        """Получение данных о номере телефона
        :param: `self.__check_mnp_link:` str — Адрес сайта для получения данных по номеру телефона.
        :return: `__result_number_data:` dict - Данные клиента.
        """

        # Получение данных MNP по номеру тел. клиента 
        try:
            __result_number_data = requests.get(self.__check_number_link + user_number)
        
            if __result_number_data.ok:
                __result_number_data: dict = __result_number_data.json()

            else:
                __result_number_data: dict = {"status_error": True}

        except requests.exceptions.ConnectionError as connection_error:
            __result_number_data: dict = {"status_error": True}
        
        return __result_number_data

    # Ввод данных в консоль
    @property
    def print_number_results(self) -> str:
        """Вывод полученных данных"""

        try:
            console_clear()
            _user_number: str = input(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}1{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}' + 
                f'Введите номер телефона{COLOR_CODE["DARK"]} +79833170773: {COLOR_CODE["RED"]}').strip()
            
            # Если ввели номер телефона
            if _user_number:
                print(f'{COLOR_CODE["RED"]}[~] {COLOR_CODE["RED"]}Поиск данных.. {COLOR_CODE["RED"]}\n')
                _get_user_number_data = self.__return_number_data(user_number=_user_number)

                # Проверка статуса ошибки
                if _get_user_number_data.get("limit") <= 0:
                    print(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[!] '+
                        f'{COLOR_CODE["RED"]}К сожалению, вы израсходовали {COLOR_CODE["DARK"]}все лимиты')
                    
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Всего лимитов: {COLOR_CODE["DARK"]}'+
                        f'{str(_get_user_number_data.get("limit", self.__not_found_text))}{COLOR_CODE["RED"]}')
                
                elif _get_user_number_data.get("status_error") or _get_user_number_data.get("error"):
                    print(f'{COLOR_CODE["RED"]}[!] {COLOR_CODE["RED"]}Данные не найдены {COLOR_CODE["RED"]}\n')


                # Ввод данных о номере
                else:
                    _number_data_unknown = _get_user_number_data
                    _number_data_country = _get_user_number_data.get('country')
                    _number_data_capital = _get_user_number_data.get('capital')
                    _number_data_region = _get_user_number_data.get('region')
                    _number_data_other = _get_user_number_data.get('0')

                    if not _number_data_region:
                        _number_data_region: dict = {"autocod": self.__not_found_text, 
                        "name": self.__not_found_text,
                        "okrug": self.__not_found_text}

                    # Страна            
                    # Для украины информация о стране отсутствует
                    if _number_data_country.get("country_code3") == 'UKR':
                        print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                            f'{COLOR_CODE["RED"]}Страна:{COLOR_CODE["RED"]} Украина{COLOR_CODE["RED"]}')
                    
                    else:
                        print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                            f'{COLOR_CODE["RED"]}Страна:{COLOR_CODE["RED"]} '+
                            f'{_number_data_country.get("name", self.__not_found_text)}, ' +
                            f'{_number_data_country.get("fullname", self.__not_found_text)}{COLOR_CODE["RED"]}')

                    # Город
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Город:{COLOR_CODE["RED"]} '+
                        f'{_number_data_other.get("name", self.__not_found_text)}{COLOR_CODE["RED"]}')

                    # Почтовый индекс
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Почтовый индекс:{COLOR_CODE["RED"]} '+
                        f'{_number_data_other.get("post", self.__not_found_text)}{COLOR_CODE["RED"]}')

                    # Код валюты
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Код валюты:{COLOR_CODE["RED"]} '+
                        f'{_number_data_country.get("iso", self.__not_found_text)}{COLOR_CODE["RED"]}')

                    # Телефонные коды 
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Телефонные коды:{COLOR_CODE["RED"]} '+
                        f'{_number_data_capital.get("telcod", self.__not_found_text)}{COLOR_CODE["RED"]}')

                    # Посмотреть в wiki
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Посмотреть в wiki:{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}{COLOR_CODE["RED"]} '+
                        f'{_number_data_other.get("wiki", self.__not_found_text)}{COLOR_CODE["RED"]}')


                    # Регион номереа авто
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Гос. номер региона авто:{COLOR_CODE["RED"]} '+
                        f'{_number_data_region.get("autocod", self.__not_found_text)}{COLOR_CODE["RED"]}')

                    # Оператор
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Оператор:{COLOR_CODE["RED"]} '+
                        f'{_number_data_other.get("oper", self.__not_found_text)}, {COLOR_CODE["DARK"]}'+
                            f'{_number_data_other.get("oper_brand", self.__not_found_text)}, '+
                            f'{_number_data_other.get("def", self.__not_found_text)}{COLOR_CODE["RED"]}')
                
                    # Местоположение
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Местоположение:{COLOR_CODE["RED"]} '+
                        f'{_number_data_country.get("name", self.__not_found_text)}, ' +
                        f'{_number_data_region.get("name", self.__not_found_text)}, ' +
                        f'{_number_data_other.get("name", self.__not_found_text)}{COLOR_CODE["DARK"]} ('+
                            f'{_number_data_other.get("latitude", self.__not_found_text)}, '+
                            f'{_number_data_other.get("longitude", self.__not_found_text)}){COLOR_CODE["RED"]}')

                    # Открыть на карте (google) 
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Открыть на карте (google):{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}{COLOR_CODE["RED"]} '+
                        f'https://www.google.com/maps/place/'+
                        f'{_number_data_other.get("latitude", self.__not_found_text)}+'+
                        f'{_number_data_other.get("longitude", self.__not_found_text)}{COLOR_CODE["RED"]}')

                    # Локация 
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Локация:{COLOR_CODE["RED"]} '+
                        f'{_number_data_unknown.get("location", self.__not_found_text)}{COLOR_CODE["RED"]}')

                    # Язык
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Язык общения:{COLOR_CODE["RED"]} '+
                        f'{_number_data_country.get("lang", self.__not_found_text).title()}, '+
                            f'{_number_data_country.get("langcod", self.__not_found_text)}{COLOR_CODE["RED"]}')
            
                    # Край/Округ/Область
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Край/Округ/Область:{COLOR_CODE["RED"]} '+
                        f'{_number_data_region.get("name", self.__not_found_text)}, '+ 
                            f'{_number_data_region.get("okrug", self.__not_found_text)}{COLOR_CODE["RED"]}')                     

                    # Столица
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Столица:{COLOR_CODE["RED"]} '+
                        f'{_number_data_capital.get("name", self.__not_found_text)}{COLOR_CODE["RED"]}')

                    # Широта/Долгота
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Широта/Долгота:{COLOR_CODE["RED"]} '+
                        f'{_number_data_other.get("latitude", self.__not_found_text)}, '+
                        f'{_number_data_other.get("longitude", self.__not_found_text)}{COLOR_CODE["RED"]}')
                    
                    # Отзывы о номере
                    _phone_radar = PhoneRadar(user_number=_user_number)
                    _phone_rating, _rating_link = _phone_radar.get_rating
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Оценка номера в сети:{COLOR_CODE["RED"]} '+
                        f'{_phone_rating}{COLOR_CODE["RED"]}{COLOR_CODE["RED"]} {_rating_link}{COLOR_CODE["RED"]}')
                    
                    print(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] {COLOR_CODE["RED"]}Проверьте эти ссылки (Мессенджеры и Социальные сети): {COLOR_CODE["RED"]}')
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}0{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}{COLOR_CODE["RED"]}https://www.instagram.com/accounts/password/RED{COLOR_CODE["RED"]}{COLOR_CODE["DARK"]} - Поиск аккаунта в Instagram')
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}1{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}{COLOR_CODE["RED"]}https://api.whatsapp.com/send?phone={COLOR_CODE["RED"]}{_user_number}{COLOR_CODE["RED"]}&text=Привет,%20это%20%20silent!{COLOR_CODE["RED"]}{COLOR_CODE["DARK"]} - Поиск номера в WhatsApp')
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}2{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}{COLOR_CODE["RED"]}https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar{COLOR_CODE["RED"]}{COLOR_CODE["DARK"]} - Поиск аккаунта FaceBook')
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}3{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}{COLOR_CODE["RED"]}https://www.linkedin.com/checkpoint/rp/request-password-RED?{COLOR_CODE["RED"]}{COLOR_CODE["DARK"]} - Поиск аккаунта Linkedin')
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}4{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}{COLOR_CODE["RED"]}https://ok.ru/dk?st.cmd=anonymRecoveryStartPhoneLink{COLOR_CODE["RED"]}{COLOR_CODE["DARK"]} - Поиск аккаунта OK')
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}5{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}{COLOR_CODE["RED"]}https://twitter.com/account/begin_password_RED{COLOR_CODE["RED"]}{COLOR_CODE["DARK"]} - Поиск аккаунта Twitter')
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}6{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}{COLOR_CODE["RED"]}https://viber://add?number={COLOR_CODE["RED"]}{_user_number}{COLOR_CODE["RED"]}{COLOR_CODE["DARK"]} - Поиск номера в Viber')
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}7{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}{COLOR_CODE["RED"]}https://skype:{COLOR_CODE["RED"]}{_user_number}{COLOR_CODE["RED"]}?call{COLOR_CODE["RED"]}{COLOR_CODE["DARK"]} - Звонок на номер с Skype')
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}8{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}{COLOR_CODE["RED"]}https://t.me/{COLOR_CODE["RED"]}{_user_number}{COLOR_CODE["RED"]}{COLOR_CODE["DARK"]} - Открыть аккаунт в Телеграмме')
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}9{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}{COLOR_CODE["RED"]}tel:{COLOR_CODE["RED"]}{_user_number}{COLOR_CODE["RED"]}{COLOR_CODE["DARK"]} - Звонок на номер с телефона')
                
                    # Всего лимитов
                    print(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[+] '+
                        f'{COLOR_CODE["RED"]}Всего лимитов: '+
                        f'{str(_get_user_number_data.get("limit", self.__not_found_text))}{COLOR_CODE["RED"]}')

                    input(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}' + 
                        f'Чтобы завершить поиск, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RED"]}ENTER ')
            
            # Если не ввели номер телефона
            else:
                print(f'{COLOR_CODE["RED"]}[!] {COLOR_CODE["RED"]}Ошибка, введите номер телефона! {COLOR_CODE["RED"]}\n')

        except KeyboardInterrupt:
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["RED"]}Вынужденная остановка работы! {COLOR_CODE["RED"]}\n')

