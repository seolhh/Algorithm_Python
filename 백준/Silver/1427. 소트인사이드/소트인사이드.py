import sys
input = sys.stdin.readline
n = sorted(input().rstrip(),reverse=True)
print(''.join(n))