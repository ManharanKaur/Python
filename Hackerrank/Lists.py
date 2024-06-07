#Lists
if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        ip = input()
        if ip.startswith('insert'):
            ip = ip.split()
            index = int(ip[1])
            value = int(ip[2])
            l.insert(index, value)
        elif ip == 'print':
            print(l)
        elif ip.startswith('remove'):
            ip = ip.split()
            index = int(ip[1])
            l.remove(index)
        elif ip.startswith('append'):
            ip = ip.split()
            index = int(ip[1])
            l.append(index)
        elif ip == 'sort':
            l.sort()
        elif ip == 'pop':
            l.pop()
        elif ip == 'reverse':
            l.reverse()
