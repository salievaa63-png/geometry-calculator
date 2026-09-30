import math

S = 0.0
for n in range(1, 51):
    tg_val = math.tan(2 * n + math.pi / 2)
    fact = math.factorial(n + 1)
    S += tg_val / fact

print(f"Сумма S = {S:.6f}")
