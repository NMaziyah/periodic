#!/usr/bin/env python

import random
#used random method 

def main():
#function def

    """PERIODIC TABLE"""
    #tajuk program

    print("Guess Reactive Nonmetals From Periodic Table")
    #paparan arahan untuk pengguna

    chem=[
        "hydrogen",
        "carbon",
        "nitrogen",
        "oxygen",
        "fluorine",
        "phospherate",
        "sulfur",
        "chlorine",
        "selenium",
        "bromine",
        "iodine"]
    #senarai untuk pilihan 

    g=random.choice(chem)
    #random method choice variable g menyimpan info dari senarai chem 
    #print(g)
    guess=None
    #setkan variable guess kepada tiada nilai

    while g != guess:
    #while untuk ulangan 

        guess=str(input("Name one reactive nonmetals from periodic table: "))
        #pengguna memasukkan satu nama

        if g==guess:
            print("Congratulations!!!")
            print("You guessed {}. Congratulations you got it right!".format(guess))
        else:
            print("Please try again...")
            print("You guessed {}. Sorry that's wrong answer, please try again!".format(guess))
main()
