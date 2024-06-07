# Introduction to Sets
def average(array):
    "{:.3f}".format(sum(set(array))/len(set(array)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)