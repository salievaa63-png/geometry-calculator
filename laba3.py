import math

def f(x):
    if x < 0:
        return x**2 + 1
    else:
        return math.sin(x)

print("Четный вариант (while do):")
x = -5
while x <= 5:
    print(f"x={x:.1f}, y={f(x):.5f}")
    x += 0.5

print("\nНечетный вариант (repeat until):")
x = -5
while True:
    print(f"x={x:.1f}, y={f(x):.5f}")
    x += 0.5
    if x > 5:
        break
