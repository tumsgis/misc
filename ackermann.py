#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tumi Snær Gíslason
# Nov 30, 2014

# The ackermann function

# From wikipedia:
# In computability theory, the Ackermann function, named after Wilhelm Ackermann, 
# is one of the simplest[1] and earliest-discovered examples of a total computable 
# function that is not primitive recursive. All primitive recursive functions are 
# total and computable, but the Ackermann function illustrates that not all total 
# computable functions are primitive recursive.

# Definition, for non-negative numbers m,n
# 
#           n+1                 if m = 0
#   A =     A(m-1, 1)           if m > 0 and n = 0
#           A(m-1, A(m, n-1))   if m > 0 and n > 0

import sys

# (funcName, m, n)
# m, n >= 0
_args = sys.argv[1:]    # catch all except 'ackermann.py'





# Recursive implementation
# Bad, really quickly exceeds maximum recursion depth
def rec_acker(m, n):

    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return rec_acker(m-1, 1)
    if m > 0 and n > 0:
        return rec_acker(m-1, rec_acker(m, n-1))







# Iterative, "dynamic programming style" implementation

# In on of the cases of the ackermann function we get
# A(m-1, A(m, n-1)).
# So, in that case, we store the m-1 value, while we calculate the A(m, n-1)
# part.

def dyn_acker(m, n):

    # quick cases
    if m == 0:
        return n + 1
    if m == 1:
        return n + 2

    waiting_funcs = [] # stores values of m, waiting for the n value, used as a stack
    top_func = -1       # on top of the stack
    seq = {}        # sequences of the same number (the idea comes from compression)
    seq_index = -1         # sequence index

    func_to_calc = ()

    while True:
        
        if func_to_calc:
            m = func_to_calc[0]
            n = func_to_calc[1]
            func_to_calc = ()

        if m > 0 and n == 0:        # A(m-1, 1) if m > 0 and n = 0
            m -= 1
            n = 1

        elif m > 0 and n > 0:       # A(m-1, A(m, n-1)) if m > 0 and n > 0

            new_m = m - 1

            if m == 1:
                func_to_calc = (0, n+1)
            elif new_m != top_func:
                seq_index += 1
                seq[seq_index] = 1
                waiting_funcs.append(new_m)
                top_func = new_m
                func_to_calc = (m, n-1)
            else :
                seq[seq_index] += 1
                func_to_calc = (m, n-1)


        elif m == 0:                # n+1 if m = 0
            if not waiting_funcs:
                return n + 1
            else:
                m = top_func
                n += 1
                if seq[seq_index] == 1:
                    del seq[seq_index]
                    seq_index -= 1
                    waiting_funcs.pop()
                    if waiting_funcs:
                        top_func = waiting_funcs[-1]
                else :
                    seq[seq_index] -= 1






def main():

    d_funcCalls = {
        'rec_acker' : rec_acker,
        'dyn_acker' : dyn_acker
    }
    
    (funcName, m, n) = _args
    
    func = d_funcCalls[funcName]

    # inputs m, n are strings
    m = int(m)
    n = int(n)

    print func(m,n)


if __name__ == "__main__":
    main()





# $ time python ackermann.py dyn_acker 4 1
# 65533

# real    0m0.144s
# user    0m0.132s
# sys     0m0.008s
