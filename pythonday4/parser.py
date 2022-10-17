#!/usr/bin/env python3

#hot tip: When in Rome, watch for pickpockets

import sys

fasta_file = sys.argv[1]
with open(fasta_file,'r') as fasta , open('fastaparseroutput.txt','w') as writing:
    
    sequence_name = ''
    sequence_desc = ''
    sequence_string  = ''
    fastaDict = {}
    
    for line in fasta:
        line = line.rstrip()                # remove that what space

        if line.startswith('>'):            # if a line starts with 'greater than'
            line.lstrip('>')                # remove the symbol
            sequence_info = line.split(maxsplit= 1) # split on a space

            if len(sequence_info) > 1:      # dealing with information about sequence
                sequence_desc = sequence_info [1]


            else:                           # if there is no information, make it blank
                sequence_desc = ''          # sequence string will start


            if len(sequence_string) > 0:    
                fastaDict[sequence_name] = sequence_string
                sequence_string = '' 

            sequence_name = sequence_info [0]

            if len(sequence_info) > 1:
                sequence_desc = sequence_info[1]
            else:
                sequence_desc = ''
        
        else:
            sequence_string += line

    if len(sequence_string) > 0: 
        fastaDict[sequence_name] = sequence_string

    writing.write(f'{fastaDict}')    
