
import sys
from utils import *




best_sell = -1
best_buy = -1





def match(orders):
    if best_sell == -1 or best_buy == -1:
        return

    bbo = orders[best_buy]
    bso = orders[best_sell]

    if bbo[FLD_PRICE] >= bso[FLD_PRICE]:
        # match



def add_order(orders, id):
    if id in orders:
        raise Exception("ID already exists %d" % id)

    o = (get_side(), get_quantity(), get_price())
    orders[id] = o

    if PRICE_INT:
        print "A,%d,%s,%d,%d" % (id, o[FLD_SIDE], o[FLD_QUANTITY], o[FLD_PRICE])
    else:
        print "A,%d,%s,%d,%.2f" % (id, o[FLD_SIDE], o[FLD_QUANTITY], o[FLD_PRICE])

    match(orders)
   


def get_random_id(orders):
    keys = orders.keys()

    b = 0
    e = len(keys)

    idx = int(rand() * (e - b)) + b
    id = keys[idx]
    return id



def remove_order(orders, id):
    o = orders[id]
    orders.pop(id)

    if PRICE_INT:
        print "X,%d,%s,%d,%d" % (id, o[FLD_SIDE], o[FLD_QUANTITY], o[FLD_PRICE])
    else:
        print "X,%d,%s,%d,%.2f" % (id, o[FLD_SIDE], o[FLD_QUANTITY], o[FLD_PRICE])
   


def modify_order(orders, id, delta):
    o = orders[id]
    o = (o[FLD_SIDE], o[FLD_QUANTITY] - delta, o[FLD_PRICE])
    orders[id] = o

    if PRICE_INT:
        print "M,%d,%s,%d,%d" % (id, o[FLD_SIDE], o[FLD_QUANTITY], o[FLD_PRICE])
    else:
        print "M,%d,%s,%d,%.2f" % (id, o[FLD_SIDE], o[FLD_QUANTITY], o[FLD_PRICE])
   
 


def modify_random_order(orders):
    if not orders:
        return

    id = get_random_id(orders)

    # I always modify down
    o = orders[id]

    # I modify by at least 1 item
    delta = int(rand() * o[FLD_QUANTITY]) + 1

    if o[FLD_QUANTITY] - delta == 0:
        remove_order(orders, id)
    else:
        modify_order(orders, id, delta)
        match(orders)
    


def remove_random_order(orders):
    if not orders:
        return 

    id = get_random_id(orders)
    remove_order(orders, id)



def main():
    N = int(sys.argv[1])

    current_ID = 31 
    orders = {}
    

    for i in range(N):
        mt = gen_msg_type() 
        if mt == 'A':
            current_ID += 1
            add_order(orders, current_ID)
        elif mt == 'M':
            modify_random_order(orders)
        else:
            remove_random_order(orders)












main()
