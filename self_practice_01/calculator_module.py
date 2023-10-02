def _calculator_module():
    pass

def _add(x ,y):
    return x + y

def _substract(x , y):
    return x - y

def _multiply(x , y):
    return x * y

def _divide(x, y):
    return x / y

def calculate(x, y, operation: str):
    match operation:
        case "+":
            return _add(x, y)
        case "-":
            return _substract(x, y)
        case "*":
            return _multiply(x, y)
        case "/":
            return _divide(x, y)
        case _:
            raise ValueError("It is an invalid operation. Please try again...")




