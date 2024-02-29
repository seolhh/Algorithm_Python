n,m = map(int,input().split())
visited = []
ans=[]
def bt(start):
    if len(visited) ==m:
        print(' '.join(map(str,visited)))
        return
    for i in range(start,n+1):
        if i not in visited:
            visited.append(i)
            bt(i+1)
            visited.pop()

bt(1)
