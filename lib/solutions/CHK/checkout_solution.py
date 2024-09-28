

# noinspection PyUnusedLocal
# skus = unicode string

import re
from math import floor


def get_value(number,price, small_deal_price=None, small_deal_quantity=None, big_deal_price=None, 
              big_deal_quantity=None,trigger_for_free=None,trigger_value=None,min_basket=None):
    if min_basket != None:
        not_free = min_basket - trigger_for_free
    else:
        not_free = 0
    if trigger_value != None:
        free = floor((trigger_value - not_free)/trigger_for_free)
    else:
        free = 0
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
        ]
    total = 0
    prices = {
        "A":50,"A_deal":130,"A_deal_ammount":3,"A_second_deal":200,"A_second_amount":5,
        "B":30,"B_deal":45, "B_deal_ammount":2,
        "C":20,
        "D":15,
        "E":40,
        "F":10, "F_deal_amount":2, "F_deal":10,
        }

    
    number_of_a = skus.count('A')
    number_of_b = skus.count('B')
    number_of_c = skus.count('C')
    number_of_d = skus.count('D')
    number_of_e = skus.count('E')
    number_of_f = skus.count('F')

    
    values = [
        get_value(number=skus.count(item['Item']),price=item['Price'],small_deal_price=item['small_deal_price'],small_deal_quantity=item['small_deal_quantity'],
                  big_deal_price=item['big_deal_price'],big_deal_quantity=item['big_deal_quantity'],trigger_for_free=item['trigger_for_free'],
                  trigger_value=skus.count(item['trigger_value']),min_basket=item['min_basket']) 
        for item in grid
        ]
    

    value_of_b = get_value(number=number_of_b,price=prices['B'],small_deal_price=45,small_deal_quantity=2,
                           trigger_for_free=2,trigger_value=number_of_e)

    value_of_c =  get_value(number_of_c,prices["C"])
    value_of_d =  get_value(number_of_c,prices['D'])
    value_of_e = (number_of_e ) * prices["E"]

    # Once you go past the 3 F mark you get the 1st F for free as well
    if number_of_f >= 3:
        value_of_f = (floor((number_of_f-1)/prices['F_deal_amount'])*prices["F_deal"] 
                      + ((number_of_f-1) % prices["F_deal_amount"])*prices['F']
                      +prices['F']) 
    else:
        value_of_f = number_of_f * prices['F']

    total = sum(values)

    if total == 0:
        return -1

    return total





