def uniqueOccurrences(lis):
    count = {}
    for i in lis:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    sol = {}

    for i in count:
        if count[i] in sol:
            sol[count[i]] += 1
        else:
            sol[count[i]] = 1
    
    for i in sol:
        if sol[i] != 1:
            return False
    return True

def checker(x):
    if int(x) >= -1000 and int(x) <=1000:
        return int(x);
    else:
        raise ValueError("Invalid Input")
        
try:
    lis = list(map(checker,input().split()))
    if len(lis) > 1000 or len(lis) < 1:
        print("Invalid size of array")
    else:
        print(uniqueOccurrences(lis))
except ValueError as e:
    print(e)
except Exception as e:
    print("An error occurred:", e)

