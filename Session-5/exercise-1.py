def count_bases(seq):
    """Counting the number of As, CS, Ts and Gs in the sequence"""

    # Counter for the As
    resulta = 0
    # Counter for the Cs
    resultc = 0
    # Counter for te Ts
    resultt=0
    # Counter for the Gs
    resultg=0

    for base in seq:

        if base == 'A':
            resulta += 1
        elif base == 'C':
            resultc += 1
        elif base == 'T':
            resultt += 1
        elif base == 'G':
            resultg += 1
          # Return the results
    results= {'A': resulta, 'C': resultc, 'T': resultt, 'G': resultg}
    return results



# Main program
s = (input('Enter the sequence: ')).upper()
n = count_bases(s)
# Calculate the total sequence lenght
tl= len(s)
print('This sequence is {} bases in lenght'.format(tl))

for key in n:
    # Calculate the percentage of As, Cs, Ts, Gs in the sequence
    if tl > 0:
        perc = round(100.0 * n[key] / tl, 1)
    else:
        perc = 0

    # Results for As, Cs, Ts, Gs bases
    print('Bases {}'.format(key))
    print('  Counter: {}'.format(n[key]))
    print('  Percentage: {}%'.format(perc))