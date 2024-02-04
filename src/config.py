import os


# Цветовая политра
COLOR_CODE = {
    "RED": "\033[31m",       # Красный
    "DARK": "\033[90m"}      # Темный

# Глоб. софт информация
GLOBAL_SOFT_INFO = {
    "AUTHOR": "Sil3nt",
    "AUTHOR_LINK": "t.me/donttrydeanonme",
    "SILENT_AUTO_BOT": "https://t.me/noblackAuto_bot",
    "SILENT_AUTO_SITE": "https://noblack-auto.ru",
    "SOFT_ORIGINAL_LINK": "https://github.com/SilentDox/Silent.git",
    "SOFT_ORIGINAL_CHANNEL": "https://t.me/silentdox",
    "SOFT_VERSION": "1.0.6",
    "BLOCKED_COUNTRIES": ["Ukraine"]}


# Очистка консоли
def console_clear() -> None:
    """Очиска консоли (Windows / Linux)"""
    
    # Очистка для Windows
    if os.sys.platform == "win32": os.system("cls")

    # Очистка для Linux
    else: os.system("clear")

# Вывод лого
def print_banner() -> None:
    """Ввод баннера"""
    console_clear()
    print(F'{COLOR_CODE["RED"]}–––––––––––––––––––––––————————')
    print(COLOR_CODE["RED"]+ "███████╗██╗██╗     ███████╗███╗   ██╗████████╗")
    print(COLOR_CODE["RED"]+ "██╔════╝██║██║     ██╔════╝████╗  ██║╚══██╔══╝")
    print(COLOR_CODE["RED"]+ "███████╗██║██║     █████╗  ██╔██╗ ██║   ██║   ")
    print(COLOR_CODE["RED"]+ "╚════██║██║██║     ██╔══╝  ██║╚██╗██║   ██║   ")
    print(COLOR_CODE["RED"]+ "███████║██║███████╗███████╗██║ ╚████║   ██║   ")
    print(COLOR_CODE["RED"] + "╚══════╝╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝" + COLOR_CODE["RED"])
    print(F'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}\n* Разработчик: {COLOR_CODE["RED"]}{COLOR_CODE["RED"]}{GLOBAL_SOFT_INFO["AUTHOR"]}{COLOR_CODE["RED"]}')
    print(F'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}* Мы в Телеграме: {COLOR_CODE["RED"]}{COLOR_CODE["RED"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_CHANNEL"]}{COLOR_CODE["RED"]}')
    print(F'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}* Оригинальная ссылка: {COLOR_CODE["RED"]}{COLOR_CODE["RED"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"]}{COLOR_CODE["RED"]}')
    print(F'{COLOR_CODE["RED"]}–––––––––––––––––––––––————————')

# Показ текст соглашения
def print_welcome_text() -> None:
    """Вывод текст о соглашении"""
    try:
        console_clear()
        agreement_file_name: str = "src/.Соглашение"
        with open(agreement_file_name, encoding="UTF-8") as file:

            print(F'{COLOR_CODE["RED"]}*–––––––––––––––––––––––————————*')
            print(F'{COLOR_CODE["RED"]}{file.read()}')
            print(F'{COLOR_CODE["RED"]}*–––––––––––––––––––––––————————*')


            try: os.remove(agreement_file_name)
            except PermissionError: 
                print(F'{COLOR_CODE["RED"]}[!] К сожалению, не получилось удалить файл, содержащий пользовательское соглашение. {COLOR_CODE["RED"]}Этот баннер будет появляться при каждом запуске.')
                
            input(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}' + 
                f'Чтобы принять соглашение, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RED"]}ENTER ')        
    
    except FileNotFoundError: ...
    except KeyboardInterrupt:
        print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["RED"]}Вынужденная остановка работы! {COLOR_CODE["RED"]}\n')
