user_input = input("Enter a string:")
print(f"You entered:{user_input}")
print(f"length of the string:{len(user_input)}")
print(f"First character of the string:{user_input[0]}")
print(f"Last character of the string:{user_input[-1]}")
mid = len(user_input)  // 2
print(f"middle character of the string:{user_input[mid]}")
even_chars = user_input[::2]
print(f"even character of the string:{user_input[::2]}")
odd_chars = user_input[1::2]
print(f"odd character of the string:{user_input[1::2]}")
reverse_chars = user_input[::-1]
print(f"reverse character of the string:{user_input[::-1]}")


