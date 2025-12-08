import random as R

List = [1, 2, 3, 4, 10, 12, 14, 16, 20, 23, 26, 29]
List1 = [-1, -2, -3, -4, -10, -12, -14, -16, -20, -23, -26, -29]

Perg = int(input ("Escreva um número de 1 a 2: "))

print(Perg)

Randy = ""

if Perg == 1:

    for _ in range(3):

        Randy = R.choice(List)

        print(f"Os números são {Randy}.")

elif Perg == 2:

    for _ in range(3):

        Randy = R.choice(List1)

        print(f"Os números são {Randy}")

else:
    print("Inicie o código de novo e escreva um número de 1 a 2.")

Perg = input("Escreva A ou B: ").upper()

print(Perg)

if Perg == "A":

    for _ in range(3):

        Randy = R.sample(List, 3)

        print(f"Os números escolhidos foram {Randy}.")

elif Perg == "B":

    for _ in range(3):

        Randy = R.sample(List1, 3)

        print(f"Os números escolhidos foram {Randy}")

else:
    print("Começe o código de novo e ESCREVA A OU B.")

Perg = input("Escreva A, B ou C: ").upper()

if Perg == "A":

    for _ in range(3):

        Randy = R.shuffle(List)

        print(f"Os números escolidos foram {Randy}.")

elif Perg == "B":

    for _ in range(3):

        Randy = R.shuffle(List1)

        print(f"Os números escolidos foram {Randy}.")

elif Perg == "C":

    for _ in range(3):

        Randy = R.sample(List, 1)
        Randy1 = R.sample(List1, 1)

        print(f"Os números escolidos foram {Randy} e {Randy1}.")

else:

    print("Execute o código de novo e ESCREVA A, B OU C.")
