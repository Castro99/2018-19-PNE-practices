#Exercise DNA I

sequence= input('Please insert a DNA sequence: ')

def dna_count(sequence):

    sequence= sequence.lower()
    number=len(sequence)

    a=sequence.count('a')
    c=sequence.count('c')
    t=sequence.count('t')
    g=sequence.count('g')

    print('Total length: ', number)
    print('A:', a)
    print('C:', c)
    print('T:', t)
    print('G:', g)

    return

dna_count(sequence)