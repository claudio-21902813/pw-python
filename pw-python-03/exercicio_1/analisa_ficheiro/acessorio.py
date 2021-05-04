def pede_nome():
    ficheiro = ''
    while True:
        ficheiro = input("Nome do ficheiro: ")
        try:
            f = open(ficheiro)
            break
        except OSError:
            print("digite um nome ficheiro existente pff")

    print(f"o nome do ficheiro e {ficheiro}")
    return ficheiro

def gera_nome(nomeFicheiro,valor_a_escrever):
    nomeArray = nomeFicheiro.split(".")
    ficheiro = open(f"{nomeArray[0]}.json","w")
    ficheiro.write(str(valor_a_escrever))
    ficheiro.close()
