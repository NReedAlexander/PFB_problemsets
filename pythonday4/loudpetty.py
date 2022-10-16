#!/usr/bin/env python3

# Hot tip: you got this
# no really, you got this


with open('Python_06.txt', 'r') as petty_song, open('louderpetty.txt', 'w') as writing:
    for line in petty_song:
        line = line.rstrip()
        line = line.upper()
        writing.write(f'{line} \n')        
    

