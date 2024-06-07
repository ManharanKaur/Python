# itertools.combinations_with_replacement()
from itertools import combinations_with_replacement
S = input().split()
r = int(S[1])
for i in sorted(list(combinations_with_replacement(sorted(S[0]),r))):
    print(''.join(i))
