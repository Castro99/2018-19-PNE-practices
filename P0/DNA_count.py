#Exercise DNA I

sequence = input('Introduce a DNA sequence to be analize: ')

def dna_length():

    sequence = sequence.upper()
    number = len(sequence)
    a = sequence.count('a')
    c = sequence.count('c')
    g = sequence.count('g')
    t = sequence.count('t')

    return number, a, c, g, t

info = dna_length()

def print_dna_length(number):
    print('Length: ', number[0])
    print('a: ', number[1])
    print('c: ', number[2])
    print('g: ', number[3])
    print('t: ', number[4])
    return

print(print_dna_length(info))