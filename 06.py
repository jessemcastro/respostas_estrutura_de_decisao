#Faça um Programa que leia três números e mostre o maior deles.

numero_1 = float(input("Digite o primeiro numero"))
numero_2 = float(input("Digite o primeiro numero"))
numero_3 = float(input("Digite o primeiro numero"))

if numero_1>numero_2 and numero_1>numero_3:
    print("O maior número é ",numero_1)
elif numero_2>numero_1 and numero_3>numero_3:
    print("O maior número é ",numero_2)
elif numero_3>numero_1 and numero_3>numero_2:
    print("O maior númeor é ",numero_3)
else:
    print("Há números iguais, digite três números diferentes")