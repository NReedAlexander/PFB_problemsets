#!/usr/bin/env python3
taxa = 'apiens, erectus, neanderthalensis'
print(taxa)
print(taxa[1])
print(type(taxa))
species =  taxa.split(', ')
print(species)
print(species[1])

print(type(species))

print(sorted(species,key=len))
