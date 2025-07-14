while True:
    expression = input('Введи математичний вираз(або "вихід" для завершення)')
    if expression.lower() == 'вихід':
        break
    result = eval(expression)
    print(f'Результат: {result}')