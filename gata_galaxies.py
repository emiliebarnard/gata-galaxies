#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
BASE_VAL = 6
WIDTH = 9
HEIGHT = 7
# From the list of unicodes, replace “+” with “000”.
# For example – “U+1F600” will become “\U0001F600”
# and prefix the unicode with “\” and print it.
# EMOJIS = ["\U0002B50", "\U0001F31F", "\U0002728" , "\U0001F4AB"] # star, glowing star, sparkles, dizzy
EMOJIS = [" "," ","⭐","✨","💫","🐾","🐈","🐈‍⬛"]
import random

def main():
    vector0 = random.choices(range(BASE_VAL), k = WIDTH)
    # print(vector0)
    rule = random.randrange(BASE_VAL ** (BASE_VAL ** 3) - 1) # TO DO: base this off of something like the date/time?
    lookup_table = gen_table(rule)
    # print(lookup_table)
    display_vectors(add_cats(ca_vector_gen(vector0, lookup_table)))

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
    vectors = [init_vector]
    prev_vector = init_vector
    for vector_num in range(HEIGHT - 1):
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
            new_vector.append(lookup_table[BASE_VAL ** 3 - 1 - dec_rep])
        vectors.append(new_vector)
        prev_vector = new_vector
    return vectors

# pick one place to replace with cat
def add_cats(vectors):
    for cat in range(random.choices([1, 2, 3, 4], weights = (70, 25, 10, 5), k = 1)[0]):
        cat_row = random.randrange(HEIGHT) #pick random row
        if BASE_VAL in vectors[cat_row]:
            vectors[cat_row][vectors[cat_row].index(BASE_VAL)] = random.choice([6,7])
        else:
            vectors[cat_row][random.randrange(WIDTH)] = random.choice([6,7])
    return vectors

def display_vectors(vectors_2d):
    for vector in vectors_2d:
        # print(' '.join(map(str, vector)))
        for number in vector:
            print(EMOJIS[number], end = "")
        print()

main()
