import random

done = False

while not done:
    print("Oque voce deseja fazer")
    print("1. Adivinha o numero")
    print("2. Sair")

    choice = input(">")
    if choice == "1":
        print("=======Adivinhe um numero de 1 a 10:\n")
        number = int(input("Digite um numero de 1 a 10\n"))
        result = random.randint(1, 10)
        if number == result:
            print("Parabens voce acertou")
        else:
            print(f"Tente novamente. O numero sorteado foi {result}")
    elif choice == "2":
        done = True
    else:
        print("Opcao invalida. Escolha uma opcao entre 1 e 2")

#F074