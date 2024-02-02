#!/usr/bin/env python3
    # print list of fib sequence up to length provided
    # if length = 3 then should print '0,1,1'
    # if length = 5 then should print '0,1,1,2,3'
    # fib_sequence, count = 0, prevCount +=1 
    # insert(i,x) i = -1, x = count + 1

def print_fibonacci(length):
    fib_list = list()
    if length == 0:
        print(fib_list)
    elif length == 1:
        fib_list = [0]
        print(fib_list)
    elif length == 2:
        fib_list = [0,1]
        print(fib_list)
    else:
        a = 0
        b = 1
        fib_list = ([a,b])
        for i in range(length - 2):
            next_num = a + b
            fib_list.append(next_num)
            a = b
            b = next_num
        print(fib_list)
            
    