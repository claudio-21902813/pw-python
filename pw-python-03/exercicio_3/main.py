import os

def calcula_tamanho_pasta(pasta):
    soma = 0

    for elemento in os.listdir(pasta):
        caminho_absoluto = os.path.join(pasta,elemento)

        if os.path.isfile(caminho_absoluto):
            soma += os.path.getsize(caminho_absoluto)
        if os.path.isdir(caminho_absoluto):
            soma = soma + calcula_tamanho_pasta(pasta)
    else:
        return soma


if __name__=="__main__":
    calcula_tamanho_pasta('C:/Users/Nuno Caetano/Desktop/Escola/SegundoSemestre/Programacao_Web/pw-python')