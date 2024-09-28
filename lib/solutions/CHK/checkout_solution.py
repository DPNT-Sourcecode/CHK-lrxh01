

# noinspection PyUnusedLocal
# skus = unicode string
from math import floor
def checkout(skus):

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

    try:
        number_of_a = skus.count('A')
    except:
        number_of_a = 0
    try:
        number_of_b = skus.count('B')
    except:
        number_of_b = 0
    try:
        number_of_c = skus.count('C')
    except:
        number_of_c = 0
    try:
        number_of_d = skus.count('D')
    except:
        number_of_d = 0


    value_of_a = floor(number_of_a/prices['A_deal_ammount'])*prices["A_deal"] + (number_of_a % prices["A_deal_ammount"])*prices['A']
    value_of_b= floor(number_of_b/prices['B_deal_ammount'])*prices["B_deal"] + (number_of_b % prices["B_deal_ammount"])*prices['B']
    value_of_c = floor(number_of_c/prices['C_deal_ammount'])*prices["C_deal"] + (number_of_c % prices["C_deal_ammount"])*prices['C']
    value_of_d = floor(number_of_d/prices['D_deal_ammount'])*prices["D_deal"] + (number_of_d % prices["D_deal_ammount"])*prices['D']

    total = value_of_a + value_of_b + value_of_c + value_of_d

    return value_of_a

