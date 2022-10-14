#!/usr/bin/env python3


#set the sets

setA = {3,14,15,9,26,5,35,9} #using squigle brackets for numbers
setB = {60,22,14,0,9}

difA = setA - setB #difference of set a
difB = setB - setA #difference of set b

# we use a pipe to find the "union" 
# think of this like "the peanut" of the vendiagram

unionAB = setA | setB


# juicy center of the vendiagram 'peanut'
sectAB = setA & setB

# the hull of the 'peanut'
symdif = setA ^ setB

print(f'''{difA} characters are found only in setA
{difB} characters are found only in setB
{unionAB} is the union of both sets
{sectAB} intersection of sets
{symdif} is the symetrical difference
''', 
 sep = ''
)




