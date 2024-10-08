

# noinspection PyUnusedLocal
# skus = unicode string

import re
from math import floor
import json


def get_value(number,price, small_deal_price=None, small_deal_quantity=None, big_deal_price=None, 
              big_deal_quantity=None,trigger_for_free=None,trigger_value=None,min_basket=None):
    
    if min_basket != None:
        not_free = min_basket - trigger_for_free

    else:
        not_free = 0
    
    # Calculate how many are free
    try:
        free = floor((trigger_value - not_free)/trigger_for_free)
        if free <0:
            free = 0
    except:
        free = 0

    number = number - free
    if number < 0:
        number = 0
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
        re.match(r'^[A-Z]+$',skus).start()
    except:
        return -1
        
    grid = [
        {'Item':'A','Price':50,'small_deal_price':130,'small_deal_quantity':3,'big_deal_price':200,'big_deal_quantity':5,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'B','Price':30,'small_deal_price':45,'small_deal_quantity':2,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':2,'trigger_value':'E','min_basket':None},
        {'Item':'C','Price':20,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'D','Price':15,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'E','Price':40,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'F','Price':10,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':2,'trigger_value':"F",'min_basket':3},
        {'Item':'G','Price':20,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'H','Price':10,'small_deal_price':45,'small_deal_quantity':5,'big_deal_price':80,'big_deal_quantity':10, 'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'I','Price':35,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'J','Price':60,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'K','Price':70,'small_deal_price':120,'small_deal_quantity':2,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'L','Price':90,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'M','Price':15,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':3,'trigger_value':'N','min_basket':None},
        {'Item':'N','Price':40,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'O','Price':10,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'P','Price':50,'small_deal_price':200,'small_deal_quantity':5,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'Q','Price':30,'small_deal_price':80,'small_deal_quantity':3,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':3,'trigger_value':'R','min_basket':None},
        {'Item':'R','Price':50,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'S','Price':20,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'T','Price':20,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'U','Price':40,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':3,'trigger_value':'U','min_basket':4},
        {'Item':'V','Price':50,'small_deal_price':90,'small_deal_quantity':2,'big_deal_price':130,'big_deal_quantity':3,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'W','Price':20,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'X','Price':17,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'Y','Price':20,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},
        {'Item':'Z','Price':21,'small_deal_price':None,'small_deal_quantity':None,'big_deal_price':None,'big_deal_quantity':None,'trigger_for_free':None,'trigger_value':None,'min_basket':None},


        ]
    total = 0  
    
    values = {item['Item']:
        get_value(number=skus.count(item['Item']),
                  price=item['Price'],
                  small_deal_price=item['small_deal_price'],
                  small_deal_quantity=item['small_deal_quantity'],
                  big_deal_price=item['big_deal_price'],
                  big_deal_quantity=item['big_deal_quantity'],
                  trigger_for_free=item['trigger_for_free'],
                  trigger_value=count_func(skus,item['trigger_value']),
                  min_basket=item['min_basket']) 
                  
         for item in grid
    }
    
    # print(values)
    checklist = [values['S'],values['T'],values['X'],values['Y'],values['Z']]
    price_list = [
        ['S',grid[18]['Price'],values['S']],
        ['T',grid[19]['Price'],values['T']],
        ['X',grid[23]['Price'],values['X']],
        ['Y',grid[24]['Price'],values['Y']],
        ['Z',grid[25]['Price'],values['Z']],
    ]
    total_list = []
    for item in price_list:
        for value in range(int(item[2]/item[1])):
            total_list.append(item[1])
    
    value_to_remove = 0
    temp_value=0
    counter = 0
    deals = 0
    total_list = sorted(total_list,reverse=True)
    print(total_list)
    while len(total_list) >0:

        
        temp_value += total_list[0]
        counter +=1
        if counter == 3:
            value_to_remove += temp_value
            deals += 1
            counter = 0
            temp_value = 0
        total_list.pop(0)
    
    total = sum(values.values())
    print(total,value_to_remove,deals)

    total = total - value_to_remove + deals*45

    return total
