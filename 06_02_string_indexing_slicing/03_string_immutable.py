name = "Erez Levran"
print(name)

print(name[0:3] + "y")
print(name + "y")
print(name)

name = "Alex"

mixed_name = "Erez Alex"
print(mixed_name)
mixed_name = mixed_name[:-2]
print(mixed_name)
mixed_name += "l"
print(mixed_name)
print(id(mixed_name))