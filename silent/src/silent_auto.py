from .config import COLOR_CODE, GLOBAL_SOFT_INFO, console_clear


def print_silent_auto_text():
    """Показ вспомогательных данных"""
    try:
        console_clear()
        print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}*{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}'
            f'Для проверки автомобилей (Сайт):{COLOR_CODE["RED"]} {GLOBAL_SOFT_INFO["SILENT_AUTO_SITE"]}')

        print(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}*{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}'
            f'Для проверки автомобилей (Телеграмм):{COLOR_CODE["RED"]} {GLOBAL_SOFT_INFO["SILENT_AUTO_BOT"]}')

        input(f'{COLOR_CODE["RED"]}{COLOR_CODE["RED"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["RED"]}] {COLOR_CODE["RED"]}' + 
            f'Чтобы завершить поиск, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RED"]}ENTER ')

    except KeyboardInterrupt:
        print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["RED"]}Вынужденная остановка работы! {COLOR_CODE["RED"]}\n')
