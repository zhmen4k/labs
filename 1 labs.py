def main():
    try:
        input_dollars = symbol(input('Введите доллары: '))
        input_percent = symbol(input('Введите процент: '))
        tip = input_dollars * input_percent
        print(f'Leave ${tip:.2f}')
        print(input_dollars, input_percent)
    except TypeError:
        print('Добавьте в ваше число символ $ или %')

def symbol(temporarily: str) -> float:
    if '$' in temporarily:
        temporarily = temporarily.replace("$", "")
        return float(temporarily)
    elif '%' in temporarily:
        temporarily = temporarily.replace("%", "")
        return float(temporarily) / 100
    else:
        print("Введен не тот символ")

main()