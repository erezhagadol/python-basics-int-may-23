#from functools import reduce
import  functools
#from functools import *
my_list = [1, 2, 3, 4, 5, 6, 7]
total = reduce(lambda x, y: x+y, my_list)
print(total)