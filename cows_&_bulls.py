# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:18:21 2020

@author: Rishabh
"""

import random

flag = 1
while flag == 1:
    num = random.randint(1000,9999)
    flag = 0
    n = str(num)
    if n[0]==n[1] or n[0]==n[2] or n[0]==n[3]:
        flag = 1
    elif n[1]==n[2] or n[1]==n[3]:
        flag = 1
    elif n[2]==n[3]:
        flag = 1

for i in range(10):
    guess = int(input("Guess Chance {0} - ".format(i+1)))
    if guess == num:
        print("CONGRATS! You win!")
        break
    else:
        ns = str(num)
        gs = str(guess)
        bcnt=0
        cc = 0
        if gs[0] in ns:
            cc+=1
            if ns[0]==gs[0]:
                bcnt+=1
                cc-=1
        if gs[1] in ns:
            cc+=1
            if ns[1]==gs[1]:
                bcnt+=1
                cc-=1
        if gs[2] in ns:
            cc+=1
            if ns[2]==gs[2]:
                bcnt+=1
                cc-=1
        if gs[3] in ns:
            cc+=1
            if ns[3]==gs[3]:
                bcnt+=1
                cc-=1
        print("You guessed {0} cow(s) and {1} bull(s).".format(cc,bcnt))
    if i == 9:
        print("You Lost. Correct Number was {}".format(num))
