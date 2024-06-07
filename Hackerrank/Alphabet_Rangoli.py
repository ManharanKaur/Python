#Alphabet Rangoli
def print_rangoli(size):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size-1, 0, -1):
        line = '-'.join(alp[n-1:i:-1] + alp[i:n])
        print(line.center(size*4-3,'-'))
    for i in range(n):
        line = '-'.join(alp[size-1: i: -1] + alp[i:n])
        print(line.center(size*4-3,'-'))
        



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)