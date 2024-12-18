import webbrowser

done = False

while not done:
    print("Oque voce deseja fazzer")
    print("1. Aprender sobre python\n")
    print("2. Aprender sobre modulos\n")
    print("3. Aprender python, fullstack js, ingles e no code\n")
    print("4. Sair")

    choice = input(">")

    if choice == "1":
        webbrowser.open("http://www.python.org")
    elif choice == "2":
        webbrowser.open("http://docs.python.org/3/py-modindex.html")
    elif choice == "3":
        webbrowser.open(
            "https://onebitcode.com/?&utm_medium=paid-traffic&utm_source=x&ltk_gcm=21276967619&ltk_gag=&ltk_gac=&ltk_gne=x&gad_source=1&gclid=CjwKCAiA34S7BhAtEiwACZzv4eLV9J0sfOQsZe8bqI5Wz9Ng45_9rLgX1VuiNDN0Aa0n0s5NZl_JtRoCVv4QAvD_BwE#detalhes-10x"
        )
    elif choice == "4":
        done = True
    else:
        print("Opçao invalida. Escolha uma opcao entre 1 a 4.")
