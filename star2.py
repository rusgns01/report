num = int(input())

for i in range(1, num):
    print(" " * (num - i) + "*" * (i * 2 - 1))
    
for i in range(num, 0, -1):
    print(" " * (num - i) + "*" * (i * 2 - 1))
