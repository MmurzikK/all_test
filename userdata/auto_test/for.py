import random 
from random import shuffle
products= [1,2,3,4,5,6,7,8,9,0]
#section = list(range(1, len(products)))
section = random.shuffle(random.randint(1, len(products)))
print (shuffle(section))

list_ = list(range(7)) #a list from 0 to 6. list() not needed in Python 2
shuffle(list_)
print(list_)