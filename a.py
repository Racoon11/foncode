
n = int(input())
m = [list(map(int, input().split())) for i in range(n)]

if n == 2:
  print(1, m[1][0] - 1)
else:
    a1 = (m[1][0] + m[2][0] - m[2][1]) // 2

    print(a1, end=' ')
    for i in range(1, n):
        print(m[0][i] - a1, end=' ')
    
