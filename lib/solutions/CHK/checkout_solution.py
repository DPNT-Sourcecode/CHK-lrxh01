

# noinspection PyUnusedLocal
# skus = unicode string

import re
from math import floor


def get_value(number,price, deal_price_1=None, deal_amount_1=None, deal_price_2=None, deal_amount_2=None):
    if deal_price_1==None:
        return number*price
    elif deal_price_1 and deal_amount_2==None:
        return floor(number/deal_amount_1)*deal_price_1 + (number % deal_amount_1)*price
    elif deal_amount_2:
        big_deals = floor(number/deal_amount_2)
        number_remaining =  number - big_deals*deal_amount_2
        small_deals = floor(number_remaining/deal_amount_1)
        remaining = number_remaining - small_deals*deal_amount_1
        print(remaining)
        return big_deals* deal_price_2 + small_deals*deal_price_1 + (remaining % deal_amount_1)*price
    else:
        return 0




def checkout(skus):

    if skus == "":
        return 0
    
    try: 
        re.match(r'^[ABCDEF]+$',skus).start()
    except:
        return -1
        
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

    
    a_5_deals = floor(number_of_a/prices['A_second_amount'])
    a_3_remaining =  number_of_a - a_5_deals*prices['A_second_amount']
    a_3_deals = floor(a_3_remaining/prices['A_deal_ammount'])
    a_remaining = a_3_remaining - a_3_deals*prices["A_deal_ammount"]
    e_deals = floor(number_of_e/2)

    if e_deals >= number_of_b:
        number_of_b = 0
    else:
        number_of_b = number_of_b - e_deals

    
    value_of_a = get_value(number_of_a,prices['A'],130,3,200,5)

    value_of_b = floor(number_of_b/prices['B_deal_ammount'])*prices["B_deal"] + (number_of_b % prices["B_deal_ammount"])*prices['B']

    value_of_c =  number_of_c * prices['C']
    value_of_d =  number_of_d *  prices['D'] 
    value_of_e = (number_of_e ) * prices["E"]

    # Once you go past the 3 F mark you get the 1st F for free as well
    if number_of_f >= 3:
        value_of_f = (floor((number_of_f-1)/prices['F_deal_amount'])*prices["F_deal"] 
                      + ((number_of_f-1) % prices["F_deal_amount"])*prices['F']
                      +prices['F']) 
    else:
        value_of_f = number_of_f * prices['F']

    total = value_of_a + value_of_b + value_of_c + value_of_d + value_of_e + value_of_f

    if total == 0:
        return -1

    return total


