# Модуль для расчета результатов

# Здесь должен быть твой код
def ruffie(result, one, two, age):
    pulse = (4 * (result + one + two) - 200) / 10
    print("asdsad")
    print(result)
    print(one)
    print(two)
    if int(age) >= 15:
        if pulse >= 15:
            return pulse, "Низкий"

        if pulse >= 11 and pulse <= 14:
            return pulse, "Удовлетворительный"

        if pulse >= 6 and pulse <= 10:
            return pulse, "Средниый"

        if pulse >= 1 and pulse <= 5:
            return pulse, "Выше среднего"

        if pulse <= 0:
            return pulse, " \n dead inside \n 1000 - 7???"

    if int(age) == 13 or 14:
        if pulse >= 17:
            return pulse, "Низкий"

        if pulse >= 13 and pulse <= 16:
            return pulse, "Удовлетворительный"

        if pulse >= 9 and pulse <= 12:
            return pulse, "Средниый"

        if pulse >= 2 and pulse <= 8:
            return pulse, "Выше среднего"

        if pulse <= 0:
            return pulse, " \n dead inside \n 1000 - 7???"

    if int(age) == 11 or 12:
        if pulse >= 18:
            return pulse, "Низкий"

        if pulse >= 14 and pulse <= 17:
            return pulse, "Удовлетворительный"

        if pulse >= 9 and pulse <= 13:
            return pulse, "Средниый"

        if pulse >= 4 and pulse <= 8:
            return pulse, "Выше среднего"

        if pulse <= 0:
            return pulse, " \n dead inside \n 1000 - 7???"
    
    if age >= 9 or 10:
        if pulse >= 20:
            return pulse, "Низкий"

        if pulse >= 16 and pulse <= 19:
            return pulse, "Удовлетворительный"

        if pulse >= 11 and pulse <= 15:
            return pulse, "Средниый"

        if pulse >= 5 and pulse <= 10:
            return pulse, "Выше среднего"

        if pulse <= 0:
            return pulse, " \n dead inside \n 1000 - 7???"
        
    if age >= 7 or 8:
        if pulse >= 21:
            return pulse, "Низкий"

        if pulse >= 17 and pulse <= 20:
            return pulse, "Удовлетворительный"

        if pulse >= 12 and pulse <= 16:
            return pulse, "Средниый"

        if pulse >= 6 and pulse <= 11:
            return pulse, "Выше среднего"

        if pulse <= 0:
            return pulse, " \n dead inside \n 1000 - 7???"
