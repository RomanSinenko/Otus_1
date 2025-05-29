"""Функция для вычисления среднего значения из списка nums"""

def calculate_average(nums):
    """Среднее значение из списка"""
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average

digit = [10, 15, 20]
result = calculate_average(digit)
print("The average is:", result)
