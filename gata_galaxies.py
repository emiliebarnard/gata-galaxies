BASE_VAL = 5
WIDTH = 9
HEIGHT = 7

import random

def main():
    vector0_test = [0] * WIDTH
    rule_test = 30
    print(gen_table(rule_test))

# convert rule number in decimal to base BASE_VAL, thanks stackoverflow :)
# https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
def conv_number(dec_num):
    if dec_num == 0:
        return [0]
    digits = []
    while dec_num:
        digits.append(int(dec_num % BASE_VAL))
        dec_num //= BASE_VAL
    return digits[::-1]

# creates 8-bit lookup table based on the rule number
def gen_table(rule_num):
    # first convert number to base representation
    converted_num = conv_number(rule_num)
    # then generate the 8-bit lookup table
    if len(converted_num) >= 8:
        return converted_num[:8]
    else: # pad it with leading zeros
        return [0] * (8 - len(converted_num)) + converted_num

# generate the vectors based on CA encryption
def vector_gen(init_vector, rule_number):
    for i in range(WIDTH):
        x = 0




main()
