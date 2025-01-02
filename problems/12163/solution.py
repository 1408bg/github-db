n = int(input())

for _ in range(0, n):
    buf = input().split()
    print(f'god{"".join(buf[1:])}')