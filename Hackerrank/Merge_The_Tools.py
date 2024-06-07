# Merge The Tools
import textwrap as tw

def merge_the_tools(string, k):
    lis = tw.wrap(string,k)
    for i in lis:
        s= set(i)
        print(''.join(filter(lambda x: x!=-1,[(s.remove(j) == None and j) if j in s else -1 for j in i])))



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)