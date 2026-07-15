numero_secreto = 37

numero_usuario = int(input("Digite um número: "))

if numero_usuario > numero_secreto:
    print('o numero digitado e maior que o numero secreto')
elif numero_usuario < numero_secreto:
    print('o numero digitado e menor que o numero secreto')
else:
    print('Parabens, esse era o numero secreto!')