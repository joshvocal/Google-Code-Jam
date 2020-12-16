'''
Problem: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da
Idea: Just go the opposite direction of each step taken

Ex:

In:  SEEESSES
Out: ESSSEESE 
'''


def solve(t, N, P):

    res = []

    for p in P:
        if p == 'E':
            res.append('S')
        elif p == 'S':
            res.append('E')

    print('Case #{}: {}'.format(t, ''.join(res)))


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    P = str(input())
    solve(t, N, P)
