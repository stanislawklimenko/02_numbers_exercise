# 1 Creating formulas
a = 2
b = 3
c = 2
# Your formula here:
result = 6*a**3 - (8*b**2) // (4*c) + 11
assert result == 50

# 2 Floating point pitfalls
# Your solution here
a = 0.1
b = 0.2
print(f'{a} + {b} = {round(a + b, 2)}')
# This won't work:
# assert 0.1 + 0.2 == 0.3