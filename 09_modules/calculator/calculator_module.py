def _add(x, y):
    return f"{x} + {y} = {x + y}"
def _substract(x, y):
    return f"{x} - {y} = {x - y}"
def _multiply(x, y):
    return f"{x} * {y} = {x * y}"
def _divide(x, y):
    return f"{x} / {y} = {x / y}"

def calculate():
    x = int(input('add your first number'))
    y = int(input('add your second number'))
    operation = input('what is your operation')
    match operation:
        case '+':
            return _add(x, y)
        case '-':
            return _substract(x, y)
        case '*':
            return _multiply(x, y)
        case '/':
            return _divide(x, y)
        case _:
            print('You choose wrong operation')
            return False
print(calculate())