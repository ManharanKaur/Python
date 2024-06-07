#Nested Lists
dic = {}
if __name__ == '__main__':
    d = []
    s = []
    for i in range(int(input())):
        ele = []
        name = input()
        score = float(input())
        ele.append(name)
        ele.append(score)
        s.append(score)
        d.append(ele)
    s.sort()
    for i in s:
        for j in s:
            if i == j:
                continue
            else:
                seclow = j
                break
        break
    N = []
    for i in d:
        for j in i:
            if j == seclow:
                ans = i
                N.append(ans[0])
    N.sort()
    for i in N:
        print(i)
