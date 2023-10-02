list_of_names = ["Yoav", "Ron", "Aviva", "Ronen", "Dan", "Galit"]
print(list_of_names)
list_of_length = list(map(lambda x: len(x), list_of_names))
print(list_of_length)
filtered_list = list(filter(lambda x: len(x) > 4, list_of_names))
print(filtered_list)
