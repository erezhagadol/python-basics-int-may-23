def reverse(word_input):
    x = ''
    for i in range(len(word_input)):
        x += word_input[len(word_input) -1 - i]
    return x

word = input('give ma a word:\n')
x = reverse(word)
if x == word:
    print('This is a palindrome')
else:
    print('This is NOT a palindrome')