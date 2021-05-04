import os
import csv #Para escrever no ficheiro .csv

def pede_pasta():
    pasta_dir = input("Este programa analisa o tipo de ficheiros presente numa pasta. Insira o caminho para uma pasta:")
    if not os.path.isdir(pasta_dir):
        print("o que inseriu nao e uma pasta !")


def faz_calculos():
    dict = {}
    filename = "C:/Users/Nuno Caetano/Desktop/Escola/SegundoSemestre/Programacao_Web/Teorica/"
    for nome in os.listdir(filename):
        nome = os.path.splitext(nome)

        if nome[1] not in dict:
            dict[nome[1]] = {'quantidade': 1, 'volume': int(os.path.getsize(filename + nome[0] + nome[1]) / (1024))}
        else:
            dict[nome[1]]['quantidade'] += 1
            dict[nome[1]]['volume'] += int(os.path.getsize(filename + nome[0] + nome[1]) / (1024))

    return dict


def guarda_resultados():
    nome_ficheiro = input('Nome do Ficheiro: ')
    with open(f"{nome_ficheiro}.csv", 'w', newline='') as ficheiro:
        campos = ['Extensao','Quantidade','Tamanho[kByte]']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)
        writer.writeheader()

        for elemento,valor in faz_calculos().values():
            print(elemento,valor)

def faz_grafico_queijos():
    print("grafico")


def faz_grafico_barras():
    print("lollllll")
