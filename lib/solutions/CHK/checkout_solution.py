

# noinspection PyUnusedLocal
# skus = unicode string

import re
from math import floor
def checkout(skus):

    if skus == "":
        return 0
    
    try: 
        re.match(r'^[ABCDE]+$',skus).start()
    except:
        return -1
        
    total = 0
    prices = {
        "A":50,
        "A_deal":130,
        "A_deal_ammount":3,
        "A_second_deal":200,
        "A_second_amount":5,
        "B":30,
        "B_deal":45,
        "B_deal_ammount":2,
        "C":20,
        "D":15,
        "E":40,
        }

    
    number_of_a = skus.count('A')
    number_of_b = skus.count('B')
    number_of_c = skus.count('C')
    number_of_d = skus.count('D')
    number_of_e = skus.count('E')

    
    a_5_deals = floor(number_of_a/prices['A_second_amount'])
    a_3_remaining =  number_of_a - a_5_deals*prices['A_second_amount']
    a_3_deals = floor(a_3_remaining/prices['A_deal_ammount'])
    a_remaining = a_3_remaining - a_3_deals*prices["A_deal_ammount"]
    e_deals = floor(number_of_e/2)
    print(e_deals)

    if e_deals >= number_of_b:
        free_b = number_of_b
    else:
        free_b = e_deals

    print(free_b,number_of_b)
    
    
    value_of_a = a_5_deals* prices["A_second_deal"] + a_3_deals*prices["A_deal"]+ (a_remaining % prices["A_deal_ammount"])*prices['A']
    

    value_of_b= floor(number_of_b/prices['B_deal_ammount'])*prices["B_deal"] + (number_of_b % prices["B_deal_ammount"])*prices['B']
    value_of_c =  number_of_c * prices['C']
    value_of_d =  number_of_d *  prices['D'] 
    value_of_e = (number_of_e ) * prices["E"]

    print(value_of_a,value_of_b,value_of_c,value_of_d)

    total = value_of_a + value_of_b + value_of_c + value_of_d + value_of_e - free_b*prices["B"]

    if total == 0:
        return -1

    return total
