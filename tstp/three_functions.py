import math
def student(): 
    fname = input('What is your first name?\n')
    length_fname = len(fname)
    length_fname = int(length_fname)

    lname = input('What is your last name?\n')
    length_lname = len(lname)
    length_lname = int(length_lname)

    print('Welcome {} {}!'.format(fname,lname))

def multiple(num1, num2):
    num1=input('Enter the first number')
    num2=input('Enter the second number')
    return num1 * num2