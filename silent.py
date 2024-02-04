try:
    # Проверка на наличие модулей
    from src.config import COLOR_CODE, GLOBAL_SOFT_INFO, print_banner, print_welcome_text
    from src.httpweb_ip import HttpWebIp
    from src.httpweb_mnp import HttpWebMnp
    from src.httpweb_number import HttpWebNumber
    from src.blocked_countries import BlockedCountries
    from src.update.update import Update
    from src.silent_auto import print_silent_auto_text
    from time import sleep
    import requests, bs4


except ImportError:
    # Совет по установке модулей и выход
    print(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[!] {COLOR_CODE["DARK"]}ВНИМАНИЕ У ВАС ПРОБЛЕМКА, НО МЫ ЕГО РЕШИМ!{COLOR_CODE["RED"]}')

    print(f'{COLOR_CODE["RED"]}[+] {COLOR_CODE["RED"]}Оригинально программное обеспечение находиться на: '+
         f'{COLOR_CODE["RED"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"]}{COLOR_CODE["RED"]}\n'+
         f'{COLOR_CODE["RED"]}[+] {COLOR_CODE["RED"]}'+
         f'Мы в телеграмме: {COLOR_CODE["RED"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_CHANNEL"]}{COLOR_CODE["RED"]}')
    
    exit(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["RED"]}У вас отсутствует модули: '+
         f'{COLOR_CODE["RED"]}requests{COLOR_CODE["RED"]} и/или {COLOR_CODE["RED"]}'+
         f'bs4{COLOR_CODE["RED"]}. {COLOR_CODE["RED"]}\n[*] {COLOR_CODE["RED"]}'+
         f'Напишите в терминал/консоль: {COLOR_CODE["RED"]}apt-get install python3-pip && pip3 install requests bs4{COLOR_CODE["RED"]}')


if __name__ == "__main__":
    # Показ текст соглашении
    print_welcome_text()

    while True:
        # Показ баннера
        print_banner()

        # Меню управления
        print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[1] {COLOR_CODE["RED"]}'
            f'Проверить {COLOR_CODE["RED"]}Номер{COLOR_CODE["RED"]} телефона.{COLOR_CODE["RED"]}\n'
            
            f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[2] {COLOR_CODE["RED"]}'
            f'Проверить {COLOR_CODE["RED"]}MNP{COLOR_CODE["RED"]} телефона.{COLOR_CODE["RED"]}\n'
            
            f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[3] {COLOR_CODE["RED"]}'
            f'Проверить {COLOR_CODE["RED"]}IP{COLOR_CODE["RED"]} телефона.{COLOR_CODE["RED"]}\n')


        try:
        
            # Выбор варианта поиска
            user_chooice: str = input(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[–] {COLOR_CODE["RED"]}'
                f'Выберите вариант поиска: {COLOR_CODE["RED"]}').strip()
            
            # Поиск по номеру телефона
            if not user_chooice or user_chooice == "1":
                httpweb_number = HttpWebNumber()
                httpweb_number.print_number_results
                sleep(3)

            # Поиск MNP по номеру телефона
            elif user_chooice == "2":
                httpweb_number = HttpWebMnp()
                httpweb_number.print_mnp_results
                sleep(3)

            # Поиск по IP
            elif user_chooice == "3":
                httpweb_number = HttpWebIp()
                httpweb_number.print_ip_results
                sleep(3)

                # Проверка обновлении
                Update().get()
                
                input(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}' + 
                  f'Чтобы вернуться назад, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RED"]}ENTER ')

            # Повторный опрос
            else: continue

        except KeyboardInterrupt:
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["RED"]}Вынужденная остановка работы! {COLOR_CODE["RED"]}\n')
            break
