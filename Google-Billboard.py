#!/usr/bin/env python
# -*- coding: utf-8 -*-
#William Ambrozic 2018
from decimal import *

def isPrime(n): #Simple Prime Checker O(sqrt(n)) Time Complexity
    '''To check if a number is prime all you need to know is the floor of the square root
    and iterate whilst checking if there are any divisors other than 1. Normally you would 
    have some initial if statements like if (n == 1) return False; however since I only care
    about a 10 digit prime in consecutive digits of e there should never be a point were it 
    calculates any n smaller than 10¹⁰. also since e starts with a 2, 1 wont even be a concern if 
    somenone wanted to calculate the first single digit prime. so do not be alarmed if this method 
    does not follow conventions.
    '''
    i = int(n**(0.5)) 
    for x in range(2,i):
        if (n % x == 0):
            return False
    return True

def Factorial(n): #Simple Calculation
    f = Decimal(1)
    for x in range(1,n+1):
        f *= Decimal(x)
    return f

def calc(c):
    eMac, eBrother, e, n = Decimal(0.00), Decimal(0.00), "2", 0
    for n in range(0, getcontext().prec):
        if len(e) >= c and isPrime(int(e)):
            return e;
        eMac += (Decimal(1)/Factorial(n)) #Calculating with the Maclaurin Series for y = eˣ | x=1
        eBrother += Decimal(2*n+2)/Factorial(2*n+1) #Calculating with the Brothers Formulae
        try:
            if str(eMac)[n] == str(eBrother)[n] and n-20 > 0:
                if len(e) >= c:
                    e = e[1:] #removing first digit in search if we passed the desired length of prime
                e += str(eMac)[n-20] #adding next digit of e
        except IndexError: #an IndexError here implies the two digits are not equal becuase one or both are null
                           #I only care when they are equal
            continue
    return 0

def main():
    getcontext().prec = 150 #Example percision for the digits of e (150 is all you need to get the answer)
    print(calc(10))
main()
