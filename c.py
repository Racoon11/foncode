n = int(input())
ans = [1]
i = 1
while len(ans) != n:
    i += 1
    if sum(map(int, str(i))) == len(str(i)):
        ans.append(i)
print(*ans)
