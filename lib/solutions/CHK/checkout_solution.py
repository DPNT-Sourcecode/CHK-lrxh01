

# noinspection PyUnusedLocal
# skus = unicode string

import re
from math import floor


def get_value(number,price, small_deal_price=None, small_deal_quantity=None, big_deal_price=None, 
              big_deal_quantity=None,trigger_for_free=None,trigger_value=None,min_basket=None):
    
    if min_basket != None:
        not_free = min_basket - trigger_for_free
        print(not_free)  
    else:
        not_free = 0
    if trigger_value != None and number >= trigger_for_free:
        free = floor((trigger_value - not_free)/trigger_for_free)
        number = number - free

    
    if small_deal_price==None:
        return number*price
    elif small_deal_price and big_deal_quantity==None:
        return floor(number/small_deal_quantity)*small_deal_price + (number % small_deal_quantity)*price
    elif big_deal_quantity:
        big_deals = floor(number/big_deal_quantity)
        number_remaining =  number - big_deals*big_deal_quantity
        small_deals = floor(number_remaining/small_deal_quantity)
        remaining = number_remaining - small_deals*small_deal_quantity
        return big_deals* big_deal_price + small_deals*small_deal_price + (remaining % small_deal_quantity)*price
    else:
        return 0

def count_func(skus, letter):
        if letter == None:
            return None
        else: 
            return skus.count(letter)

def checkout(skus):

    if skus == "":
        return 0
    
    try: 
        re.match(r'^[ABCDEF]+$',skus).start()
    except:
        return -1
        
    grid = [
        {'Item':'A','Price':50,'small_deal_price':130,'small_deal_quantity':3,'big_deal_price':200,'big_deal_quantity':5,
        'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'B','Price':30,'small_deal_price':45,'small_deal_quantity':2,'big_deal_price':None,'big_deal_quantity':None,
        'trigger_for_free':2,'trigger_value':'E','min_basket':None},
        {'Item':'C','Price':20,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,
        'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'D','Price':15,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,
        'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'E','Price':40,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,
        'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'F','Price':10,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,
        'trigger_for_free':2,'trigger_value':"F",'min_basket':3},

        ]
    total = 0  
    
    values = [
        get_value(number=skus.count(item['Item']),price=item['Price'],small_deal_price=item['small_deal_price'],small_deal_quantity=item['small_deal_quantity'],
                  big_deal_price=item['big_deal_price'],big_deal_quantity=item['big_deal_quantity'],trigger_for_free=item['trigger_for_free'],
                  trigger_value=count_func(skus,item['trigger_value']),min_basket=item['min_basket']) 
        for item in grid
        ]


    total = sum(values)
    print(values)

    return total


