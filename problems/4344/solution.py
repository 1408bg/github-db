n = int(input())

for _ in range(n):
    buf = list(map(int, input().split()))
    total = sum(buf[1:])
    avg = total / buf[0]
    cnt = 0
    for score in buf[1:]:
        if score > avg:
            cnt+=1
    ratio = round((cnt / total) * 100, 3)
    print(f"{ratio}%")