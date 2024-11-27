#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
   while True:
        print("10")
        print("9")
        print("8")
        print("7")
        print("6")
        print("5")
        print("4")
        print("3")
        print("2")
        print("1")
        print("Happy New Year!")
        break
happy_new_year()      
        
    

def square_integers(int_list):
    # code goes here!
      int_list = [1,2,3,4,5]
      return [i**2 for i in int_list]



def fizzbuzz():
    # code goes here!
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    
