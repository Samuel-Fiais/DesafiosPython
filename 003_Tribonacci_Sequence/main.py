def tribonacci(signature, n):
    res = signature[:n]
    for aux in range(0, n - 3): res.append(sum(res[-3:]))
    return res

print(tribonacci([3, 2, 1], 10))