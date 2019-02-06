#Exercise DNA II

with open('DNA.csv', 'r') as f:
    for series in f:
        def dna_length():
            number = length(series.replace('\n', ''))
            a = series.count('a')
            c = series.count('c')
            g = series.count('g')
            t = series.count('t')
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