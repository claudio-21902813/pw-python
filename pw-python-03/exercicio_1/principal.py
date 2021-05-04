from exercicio_1.analisa_ficheiro import *
from exercicio_1.analisa_ficheiro.calculos import *
import json

def main():
    #ficheiro : teste_ex1.txt
    valor = pede_nome()
    info = dict()

    info["nr de linhas"] = calcula_linhas(valor)
    info["nr de caracteres"]=calcula_carateres(valor)
    info["ocorrencia de letras"] = calcula_ocorrencia_de_letras(valor)
    info["palavra_comprida"]=calcula_palavra_comprida(valor)

    info = json.dumps(info)
    gera_nome(valor,info)

if __name__ == "__main__":
    main()