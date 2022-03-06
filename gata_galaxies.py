BASE_VAL = 5
WIDTH = 9
HEIGHT = 7

import random

def main():
    vector0_test = [1, 0, 0, 0, 0, 0, 0, 0, 0]
    rule_test = 124
    lookup_table = gen_table(rule_test)
    display_vectors(ca_vector_gen(vector0_test, lookup_table))

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

# creates lookup table based on the rule number
def gen_table(rule_num):
    # first convert number to base representation
    converted_num = conv_number(rule_num)
    # then generate the 8-bit lookup table
    if len(converted_num) >= BASE_VAL ** 3:
        return converted_num[:BASE_VAL ** 3]
    else: # pad it with leading zeros
        return [0] * (BASE_VAL ** 3 - len(converted_num)) + converted_num

# generate the vectors based on CA encryption
def ca_vector_gen(init_vector, lookup_table):
    vectors = []
    prev_vector = init_vector
    for vector_num in range(HEIGHT):
        new_vector = []
        #iterate through the numbers in the vector and update the values
        for vector_elem_index in range(WIDTH): # assumes init_vector is of length WIDTH
            # need to pull info from neighbor + current cells to apply the ca ecryption -
            # grab indices, deal with wrap-around
            p_index = (vector_elem_index - 1) % WIDTH # left
            q_index = vector_elem_index % WIDTH # center
            r_index = (vector_elem_index + 1) % WIDTH # right
            # generate new cell based on lookup table:
            # grab decimal representation of the value from p, q, r
            dec_rep = BASE_VAL**2 * prev_vector[p_index] + BASE_VAL * prev_vector[q_index] + prev_vector[r_index] # base^2, base^1, base^0
            max_val = BASE_VAL ** 2 * (BASE_VAL - 1) + BASE_VAL * (BASE_VAL - 1) + (BASE_VAL - 1)
            new_vector.append(lookup_table[BASE_VAL ** 3 - 1 - dec_rep])
        vectors.append(new_vector)
        prev_vector = new_vector
    return vectors

def display_vectors(vectors_2d):
    for vector in vectors_2d:
        print(' '.join(map(str, vector)))

main()
