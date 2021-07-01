import time
#def foo(tom):
#    fred = 0
#    for bill in range(1, tom+1):
#       barney = bill
#        fred = fred + barney
#    return fred
#print(foo(10))

#def sum_of_n(n):
#    the_sum = 0
#    for i in range(1,n+1):
#        the_sum = the_sum + (i+2)
#    return the_sum
#print(sum_of_n(20))



# def sum_of_n_2(n):
#     start = time.time()
#     the_sum = 0
#     for i in range(1, n+1):
#         the_sum = the_sum + i
#         end = time.time()
#     return the_sum,end-start
#     for i in range(5):
#         print("Sum is %d required %10.7f seconds" % sum_of_n_2(10000))

def sum_n (n):
    start = time.time()
    sum1 = 0
    for i in range (1,n+1):
        sum1 = sum1 + i
        end = time.time()
    return sum1, end - start