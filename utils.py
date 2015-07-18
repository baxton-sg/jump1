


import random as r


PROB_ADD = .6
PROB_REMOVE = .1
PROB_MODIFY = .3


FLD_SIDE = 0
FLD_QUANTITY = 1
FLD_PRICE = 2


PRICE_INT = True
PRICE_MIN = 10
PRICE_MAX = 10000

QUANT_MIN = 1
QUANT_MAX = 100





# returns a rundom number in [0-1]
# I use this function to be able to switch 
# to other random numbers generator quickly
def rand():
    return r.random()



def gen_msg_type():
    n = rand()
    if n <= PROB_REMOVE:
        return 'X'
    elif n <= (PROB_REMOVE + PROB_MODIFY):
        return 'M'
    else:
        return 'A'



def get_price():
    if PRICE_INT:
        return int(rand() * (PRICE_MAX - PRICE_MIN)) + PRICE_MIN
    return rand() * (PRICE_MAX - PRICE_MIN) + PRICE_MIN



def get_quantity():
    return int(rand() * (QUANT_MAX - QUANT_MIN)) + QUANT_MIN



def get_side():
    s = rand()
    if s < .5:
        return 'B'
    return 'S'








