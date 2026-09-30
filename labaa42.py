import math

P = 1.0
for n in range(1, 11):
    chislitel = n**2 + math.sin(n * math.pi / 2)
    znamenatel = n**2 + n
    P *= chislitel / znamenatel

print(f"Произведение P = {P:.6f}")