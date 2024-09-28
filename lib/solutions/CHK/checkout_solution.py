

# noinspection PyUnusedLocal
# skus = unicode string

import re
from math import floor
def checkout(skus):

    if skus == "":
        return 0
    re.match(r'^[ABCD]+$',skus).start()
    try: 
        re.match(r'^[ABCD]+$',skus).start()
        return -1
    except:
        
        total = 0
        prices = {
            "A":50,
            "A_deal":130,
            "A_deal_ammount":3,
            "B":30,
            "B_deal":45,
            "B_deal_ammount":2,
            "C":20,
            "D":15,
            }

        
        number_of_a = skus.count('A')
        number_of_b = skus.count('B')
        number_of_b = 0
        number_of_c = skus.count('C')
        number_of_c = 0
        number_of_d = skus.count('D')
        number_of_d = 0


        value_of_a = floor(number_of_a/prices['A_deal_ammount'])*prices["A_deal"] + (number_of_a % prices["A_deal_ammount"])*prices['A']
        value_of_b= floor(number_of_b/prices['B_deal_ammount'])*prices["B_deal"] + (number_of_b % prices["B_deal_ammount"])*prices['B']
        value_of_c =  number_of_c * prices['C']
        value_of_d =  number_of_d *  prices['D'] 

        total = value_of_a + value_of_b + value_of_c + value_of_d

        if total == 0:
            return -1

        return total



