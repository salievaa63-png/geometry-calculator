import math

a, b, h = -0.3, 0.7, 0.05
x = a
while x <= b + 1e-9: # Небольшая погрешность, чтобы точно попасть в 0.7
    # Формула из задания 2
    num = abs(math.sin(x) - math.cos(x))
    den = (math.sin(x**2))**3 + (math.cos(x**3))**2
    y = math.sqrt(num / den)
    
    print(f"x = {x:.2f}, y = {y:.5f}")
    x += h