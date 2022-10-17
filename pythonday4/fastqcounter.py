#!/usr/bin/env python3

#hot tip: you code better after you run
#hot tip: you code better when you eat regularly

with open('Python_06.fastq', 'r') as fasta, open('counter.txt', 'w') as output:

    linecount = 0    
    charcount = 0
   
    for line in fasta:
        linecount += 1
        charcount += len(line)

    avglen = charcount / linecount

    output.write(f'total lines:\t{linecount}\ncharacter count:\t{charcount}\naverage line length:\t{avglen}')
