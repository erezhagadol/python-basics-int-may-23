import add
def multi(num_1, num_2):
    a = 0
    for i in range(num_2):
        a = add.add(a, num_1)
    return a


if __name__== "__main__":
    print(multi(2,4))





