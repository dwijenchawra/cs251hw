import math

def hash_function(k):
    A = 0.6180
    return math.floor(10 * (k * A % 1))

num2hash = [1028, 2308, 5763, 2023, 1953, 6033, 8958, 3408, 6003]

for num in num2hash:
    print("num: ", num, "hash: ", hash_function(num))
print()
num2hash = [6033, 5763]

for num in num2hash:
    print("num: ", num, "hash: ", hash_function(num))
print()
num2hash = [4959, 7634]

for num in num2hash:
    print("num: ", num, "hash: ", hash_function(num))