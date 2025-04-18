numbers=list(map(int,input().split()))
result = {i: 0 for i in range(1, 10)}
for num in numbers:
    for i in range(1, 10):
        if num % i == 0:
            result[i] += 1
for key in result:
    print(f"{key}: {result[key]}")
