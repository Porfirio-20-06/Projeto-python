numero = 20

fibonacci = [0, 1]
for i in range(2, numero):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(f'A sequência de Fibonacci até o {numero}º termo é: {fibonacci}')