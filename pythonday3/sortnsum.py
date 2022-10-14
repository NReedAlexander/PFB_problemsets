#!/usr/bin/env python3

myList = [101,2,15,22,95,33,2,27,72,15,52]

evensum = 0
oddsum = 0

for numb in myList:
    if numb % 2 == 0:
        evensum = numb + evensum
    else:
        oddsum = numb+ oddsum

print(f'''Sum of even numbers: \t  {evensum}
      Sum of odds: \t {oddsum}
      ''')
        
