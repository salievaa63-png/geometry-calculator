import math

# Заданное значение x
x = 3.76

# Вычисление числителя
numerator = 5 * (x**5) + math.exp(-x) * math.cos(5 * x)

# Вычисление знаменателя
denominator = 3 * (x**3) + (3**x) * math.sin(3 * x)

# Вычисление значения функции
y = numerator / denominator

# Вывод результата с 5 знаками после запятой
print(f"{y:.5f}")