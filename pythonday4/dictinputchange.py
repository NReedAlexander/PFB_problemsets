#!/usr/bin/env python3

import sys

fav_dict = {'book': 'spatial ecology', 'song': 'Tom Petty - The Last DJ','tree' :'sugar maple', 'organism' : 'Parrot the CAT' }

originaldict = fav_dict.copy()

fav_dict[sys.argv[1]] = sys.argv[2]

print(originaldict)

print(fav_dict)
