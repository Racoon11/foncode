def nod(a, b):
    a, b = max(a,b), min(a,b)
    while (b > 0):
    	b, a = a%b, b
    return a

n = int(input())
ans = []
ans2 = []
for i in range(n):
    a, b = map(int, input().split())
    c = nod(a, b)
    ans.append('{}/{}'.format(a//c, b//c))
    ans2.append((a//c) / (b//c))

ans = sorted(enumerate(ans), key=lambda x: ans2[x[0]])
for i in ans:
    print(i[1])
