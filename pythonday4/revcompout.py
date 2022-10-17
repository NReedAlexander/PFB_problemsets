#!/usr/bin/env Python3

# Hot tip: A bus station is where the bus stops,
#          at my desk, I have a work station...


with open('Python_06.seq.txt', 'r') as sequences, open('revcomp.txt', 'w') as writing:
    geneSet = {}
    for line in sequences:
        line = line.rstrip()
        key,seq = line.split()
        geneSet[key] = seq
    revComp = {}
    for key in geneSet:
        dna = geneSet[key]
        Aseq = dna.replace('A', 't')
        Tseq = Aseq.replace('T', 'a')
        Gseq = Tseq.replace('G', 'c')
        Cseq = Gseq.replace('C', 'g')
        Useq = Cseq.upper()
        revSeq = Cseq[::-1]
        revComp[key] = revSeq  
    for key in revComp:
        writing.write(f'>{key}\n{revComp[key]}\n')
