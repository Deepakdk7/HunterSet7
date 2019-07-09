ax=int(input())
a=list(map(int,input().split()))
u,v=list(map(int,input().split()))
print(abs(a.index(u)-a.index(v)))
