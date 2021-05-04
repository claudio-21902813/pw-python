def calcula_linhas(nomeFicheiro):
    f = open(nomeFicheiro,"r")
    return f" tem {f.readlines().__len__()} linhas"

def calcula_carateres(nomeFicheiro):
    f = open(nomeFicheiro,"r")
    return f" tem {f.read().__len__()} caracteres"

def calcula_palavra_comprida(nomeFicheiro):
    f = open(nomeFicheiro,"r")
    valor = f.readlines()
    f.close()

    valor.sort(key=len)

    return valor[-1]

def calcula_ocorrencia_de_letras(nomeFicheiro):
    f = open(nomeFicheiro,"r")
    valor = f.read()
    f.close()

    dict = {}
    for letra in valor:
        if letra not in ['\n',' ']:
            letra = letra.lower()
            if letra not in dict:
                dict[letra] = 1
            else:
                dict[letra] += 1

    return dict