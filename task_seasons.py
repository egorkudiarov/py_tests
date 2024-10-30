def check_month(month: int):
    if 1 <= month <= 2 or month == 12:
        result = 'Зима'
    elif 3 <= month <= 5:
        result = 'Весна'
    elif 6 <= month <= 8:
        result = 'Лето'
    elif 9 <= month <= 11:
        result = 'Осень'
    else:
        result = 'Некорректный номер месяца'
    return result