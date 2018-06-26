import re
from time import sleep
num = 10000

def output(list,line_num = 5):
    n = 0
    for l in list:
        if n >= line_num :
            print()
            n = 0
        n += 1
        print('{0:5s}'.format(str(l)),end= ' ')
    print('\n'+('*'*20)+'\n')

def main():
    primes = []
    l = list(range(num))
    for i in range(len(l)):
        if l[i] == 0 or l[i] == 1:
            l[i] = 'X'
            continue
        if re.search('\d',str(l[i])):
            primes.append(l[i])
            for j in range(i*2,num,l[i]):
                l[j] = 'X'
    output(primes,10)

main()
