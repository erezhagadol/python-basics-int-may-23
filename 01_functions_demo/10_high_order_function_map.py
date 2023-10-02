original_array = [2, 5, 8, 10, 25]

after_map = map(lambda  X:X ** 2, original_array)

print(original_array)
print(tuple(after_map))
print(type(after_map))
