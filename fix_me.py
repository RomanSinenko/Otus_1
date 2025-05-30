"""Функция для вычисления среднего значения из списка num"""

def calculate_average(num):
    """Среднее значение из списка"""
    total = sum(num)
    count = len(num)
    average = total / count
    return average

digit = [10, 15, 20]
result = calculate_average(digit)
print(f'The average is:, {result}')
