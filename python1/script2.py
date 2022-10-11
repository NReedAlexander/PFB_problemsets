#!/usr/bin/env python3

import sys

num = sys.argv[1]

try:
		float(num)
except ValueError :
		    print( 'please give me a number' )

if isinstance(num, int):
		n = sys.argv[1]
elif isinstance(num, str):
    n = float(sys.argv[1])


if n > 0 :
		if n > 50:
				r = n%3
				if r== 0:
						print( 'positive and greater than 50 and divisible by 3' )
				else:
						print( 'positive, greater than 50, not div by 3') 
		elif n < 50:
				r = n%2
				if r == 0 :
						print( 'positive and less than 50 and divisible by 2' )
				else :
						print( 'positive, less than 50, and not divisible by 2')
		else :
				print( 'positive and 50' )

elif n < 0 : 
		print( 'negative')
else :
    print( 'n = 0')
		

