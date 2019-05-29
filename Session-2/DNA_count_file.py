#Exercise DNA II

with open('DNA.txt', 'r') as f:
    for series in f:
        def dna_length():
            number = len(series.replace('\n', ''))
            a = series.count('A')
            c = series.count('C')
            g = series.count('G')
            t = series.count('T')
            return number, a, c, g, t

        info = dna_length()

        def print_dna_length(number):
            print('Length: ', number[0])
            print('A: ', number[1])
            print('C: ', number[2])
            print('G: ', number[3])
            print('T: ', number[4])
            return

        print(print_dna_length(info))