# Zechen Tian 1723669
# I implemented this file independently for assignment.

import random

max_key = 10**7

def gen_element():
    return random.randint(0, max_key) # an integer that is drawn uniformly at random from [0, 10^7]

def gen_push():
    return (1, gen_element())
# generate push operation

def gen_pop():
    return (2, )
# generate pop operation

def gen_getTop():
    return (3, )
# generate getTop operation

def generate_push_sequence(L):
    sequence = []
    for _ in range(L):
        sequence.append(gen_push())
    return sequence
# generate a push-only sequence of operations (for Experiment 1 and Experiment 4)

def generate_push_getTop_sequence(L, getTop_percentage):
    sequence = []
    for _ in range(L):
        if random.random() < getTop_percentage:
            sequence.append(gen_getTop())
        else:
            sequence.append(gen_push())
    return sequence
# generate sequence of operations with push and getTop (for Experiment 2)

def generate_push_pop_sequence(L, pop_percentage):
    sequence = []
    for _ in range(L):
        if random.random() < pop_percentage:
            sequence.append(gen_pop())
        else:
            sequence.append(gen_push())
    return sequence
# generate sequence of operations with push and pop (for Experiment 3)