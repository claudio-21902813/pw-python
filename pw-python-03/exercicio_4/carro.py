from exercicio_4.Automovel import Automovel

__TEXTO = "1... criar Automovel\n2...abastecer carro\n3... percorrer\n4...mostra autonomia\n5... Sair"


if __name__ == '__main__':
        carro = None
        print(__TEXTO)
        opcao = eval(input("Escolha Opcao:"))
        while True:
                if opcao == 1:
                        cap = eval(input("Capacidade: "))
                        quant_comb = eval(input("Quantidade do Combustivel: "))
                        consumo = eval(input("consumo em litros aos 100 km: "))
                        carro = Automovel.cria_automovel(cap,quant_comb,consumo)
                elif opcao == 2:
                        n_litros = eval(input("Litros: "))
                        print(carro.abastece(n_litros))
                elif opcao == 3:
                        n_km = eval(input("N_Km para percorrer: "))
                        print(carro.percorre(n_km))
                elif opcao == 4:
                        print(carro.autonomia())
                else:
                        break
                opcao = eval(input("Escolha Opcao:"))
