N = int(input())
if 0 < N and N < 10:
    for i in range(1, N + 1):
        print((( 10 ** i - 1) // 9) ** 2) # Se afiseaza numarul palindrom