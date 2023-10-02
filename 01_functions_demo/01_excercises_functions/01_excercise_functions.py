def get_text_length(name ="Hello"):
    return len(name)
print(get_text_length())

my_list = ["hello", "Erez", "Lion"]

def get_text_length_in_list(text_list):
    return sum(list(map(get_text_length, text_list)))
print(get_text_length_in_list(my_list))