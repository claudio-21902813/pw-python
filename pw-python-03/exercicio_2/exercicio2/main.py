from exercicio_2.exercicio2.analise_pasta import *

if __name__=="__main__":
    lista_chaves = [*faz_calculos().keys()]
    lista_valores = []

    for qtd in faz_calculos().values():
        lista_valores.append(qtd['quantidade'])



    faz_grafico_barras('quantidade',lista_chaves,lista_valores)
    faz_grafico_queijos('quantidade', lista_chaves, lista_valores)