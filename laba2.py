import math

a, b, h = -0.3, 0.7, 0.05

steps = int(round((b - a) / h))

print(f"{'x':>6} | {'y':>10}")
print("-" * 19)

for i in range(steps + 1):
    x = a + i * h

    num = abs(math.sin(x) - math.cos(x))
    den = (math.sin(x**2))**3 + (math.cos(x**3))**2
    y = math.sqrt(num / den)
    
    print(f"{x:6.2f} | {y:10.5f}")
