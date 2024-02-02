#!/usr/bin/env python3


    # print list of fib sequence up to length provided
    # if length = 3 then should print '0,1,1'
    # if length = 5 then should print '0,1,1,2,3'
    # fib_sequence, count = 0, prevCount +=1 
    # insert(i,x) i = -1, x = count + 1

    ## JavasScript ##
    # let array = []

    # length of 0  = 0
    # length of 1 = 0, 1
    # starting at 0 each increase in length is current count plus 
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
        i = 2
        while i < length:
            next_num = a + b
            fib_list.append(next_num)
            a = b
            b = next_num
            i += 1
        print(fib_list)
            
    