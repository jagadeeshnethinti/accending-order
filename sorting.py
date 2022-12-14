n=int(input())
a=[]
for i in range(n):
    s=int(input())
    a.append(s)
a.sort(reverse=True)
print(a)