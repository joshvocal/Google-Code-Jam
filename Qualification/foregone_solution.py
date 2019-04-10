'''
Problem: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231
Idea: Subtract the significant digit with 4 and add it to
the other number.

Ex:
N = 500
lo = 1, hi = 499

lo = 101, hi = 399
'''


def solve(t, N):
    lo = 1
    hi = N - 1

    while lo <= hi:
        if '4' in str(hi):
            power = 10**(len(str(hi)) - str(hi).index('4') - 1)
            lo += power
            hi -= power
        elif '4' in str(lo):
            lo += 1
            hi -= 1
        elif lo + hi == N:
            print("Case #{}: {} {}".format(t, lo, hi))
            break
        else:
            lo += 1
            hi -= 1


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    solve(t, N)
