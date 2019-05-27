#Exercise III P0-Extra

with open('CPLX2', 'r') as l:
    a, c, t, g = 0, 0, 0, 0
    for x in l:
        if '>' in x:
            x=''
        a += x.count('A')
        c += x.count('C')
        t += x.count('T')
        g += x.count('G')
print('A: ', a, '\nC: ', c, '\nT: ', t,'\nG: ', g)