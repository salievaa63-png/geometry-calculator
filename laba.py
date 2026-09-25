import math

x = 3.76

numerator = 5 * (x**5) + math.exp(-x) * math.cos(5 * x)

denominator = 3 * (x**3) + (3**x) * math.sin(3 * x)

y = numerator / denominator

print(f"{y:.5f}")
