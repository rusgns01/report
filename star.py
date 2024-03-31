def asterisk(n):
    if n > 1:
        asterisk(n/2)
        asteri sk(n/2)
    print("*", end='')
print(asterisk(5))
