
import requests
from ..config import GLOBAL_SOFT_INFO, COLOR_CODE
from bs4 import BeautifulSoup as bs


class Update:
    def __init__(self) -> None:
        self.__update_link: str = F'{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"][:-4]}/commits/main'

    def __str__(self) -> str:
        return F"Description: Обновляет клиент и/или уведомляет о новой версии: {self.__update_link}"

    def __repr__(self) -> str:
        return (F"Description: Обновляет клиент и/или уведомляет о новой версии: {self.__update_link}\n" +
                F"Modules: requests, bs4\n" +
                F"GITHUB/COMMITS/MAIN")
    @property
    def check(self) -> int:
        """Получение кол-во коммитов
        :param self.__update_link: Ссылка на репозиторий
        :return bs_content_len: Кол-во коммитов"""

        try:
            # Проверка обновлении по ссылке
            github_commits_content = requests.get(url=self.__update_link)
            if github_commits_content.status_code != 200:
                print(f'{COLOR_CODE["RED"]}[!] Ошибка,{COLOR_CODE["RED"]}{COLOR_CODE["RED"]} не получилось проверить наличие обновлении! {COLOR_CODE["RED"]}\n')    
                return None

            else:
                bs_content_len: int = len(bs(github_commits_content.text, "html.parser")
                .find("div", class_="container-xl")
                .find_all("li"))
                
                return bs_content_len        
        
        except requests.exceptions.ConnectionError as connection_error:
            print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[!] Ошибка,{COLOR_CODE["RED"]}{COLOR_CODE["RED"]} не получилось проверить наличие обновлении! {COLOR_CODE["RED"]}')
            return {"connection": True}
        
        except Exception as error: 
            print(f'{COLOR_CODE["RED"]}[!] Информация об ошибке: {COLOR_CODE["RED"]}')
            print(f'{COLOR_CODE["DARK"]}{error}{COLOR_CODE["RED"]}\n')
            return None
    
    def get(self):
        """Получение обновлений и обновление"""
        
        try:
            version_file_name: str = "src/update/version"
            with open(file=version_file_name, mode="r") as file_read:
                now_version = int(file_read.read().strip())
                update_checking = self.check
                if not now_version: now_version = 0
                

                # Проверка на полученние новой версии и сравнение версии
                if update_checking and type(update_checking) == int and now_version != update_checking:
                    
                    print(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[^] {COLOR_CODE["RED"]}'
                    f'Доступно новое {COLOR_CODE["RED"]}обновление!!.{COLOR_CODE["RED"]}')
                    
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[?] {COLOR_CODE["RED"]}'
                        f'Чтобы обновить, {COLOR_CODE["RED"]}удалите эту версию {COLOR_CODE["RED"]}и установите новую по исходной ссылке:{COLOR_CODE["RED"]}') 
                    
                    print(F'[*] {COLOR_CODE["RED"]}Ссылка: {COLOR_CODE["RED"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"]}')
                    
                    # Запись новых данных в файл версии
                    with open(file=version_file_name, mode="w") as file_write: 
                        file_write.write(str(self.check))

                # Новой версии еще нет
                else:
                    if not update_checking:
                        print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[*] {COLOR_CODE["RED"]}'
                        f'Новые обновлении еще не доступны.{COLOR_CODE["RED"]}')
                    
                    


        except FileNotFoundError: 
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["RED"]}Отсутствует файл "version"{COLOR_CODE["RED"]} (silent/src/update/version)')
            user_permission = input(f'{COLOR_CODE["RED"]}[?] Создать файл{COLOR_CODE["RED"]} (Да - 1 / Нет - 0): {COLOR_CODE["RED"]}')
            if not user_permission or user_permission == "1": 
                try: open("src/update/version", "w")
                except PermissionError: 
                    print(F'{COLOR_CODE["RED"]}[!] К сожалению, не получилось создать файл, обновлении. {COLOR_CODE["RED"]}Отсутствует разрешение на создание файлов (попробуйте создать файл в ручную "silent/src/update/version" и прописать там "0").')



        except ValueError:
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["RED"]}Поврежден файл "version"{COLOR_CODE["RED"]} (s/src/update/version)')
            print(f'{COLOR_CODE["RED"]}[*] {COLOR_CODE["RED"]}Проверка наличия обновлений, недоступно.{COLOR_CODE["RED"]} Переустановите софт.')
            print(F'{COLOR_CODE["RED"]}[*] {COLOR_CODE["RED"]}Ссылка: {COLOR_CODE["RED"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"]}')

        except KeyboardInterrupt:
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["RED"]}Вынужденная остановка работы! {COLOR_CODE["RED"]}\n')
