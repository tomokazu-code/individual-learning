arr = [0] * 103  # arr 用于记录方案

def dfs(n, i, a):
    if n == 0:
        print(arr[1:i])
    if i <= m:
        for j in range(a, n + 1):
            arr[i] = j
            dfs(n - j, i + 1, j)  # 请仔细思考该行含义。
#整数n分解成小于等于m 个正整数之和
# 主函数
n, m = map(int, input().split())
dfs(n, 1, 1)