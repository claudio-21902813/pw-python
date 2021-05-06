
#exercicio 4:

class Automovel():
    """ Carro que consegue descobrir descobir mostrar a distancia ate ser necessário um reabastecimento """

    __MENSAGEM_ERRO = "ERRO: Capacidade Maxima Atingida!"

    def __init__(self,cap_dep,quant_comb,consumo):
        """ Construtor da classe Carro """
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo

    def combustivel(self):
        """ devolve a quantidade de combustível no depósito """
        return self.quant_comb

    def autonomia(self):
        """devolve o numero de Km que é possível percorrer com o combustível no depósito"""
        return (int)((self.quant_comb / self.consumo ) * 100)

    def abastece(self,n_litros):
        """aumenta em n_litros o combustível no depósito e retorna a autonomia. Se este abastecimento exceder
        a capacidade do depósito, gera um erro e não aumenta a quantidade de combustível no depósito"""

        self.quant_comb += n_litros

        if self.quant_comb > self.cap_dep:
            self.quant_comb -= n_litros
            return self.__MENSAGEM_ERRO


        return self.autonomia()

    def percorre(self,n_km):
        """ percorre n_km Km, desde que a quantidade de combustível no depósito o permita,
        em caso contrário gera um erro e o trajecto não é efectuado. Retorna a autonomia."""
        print(".-._._._._._.-._._.-_+_" + "\U0001F697" + " .-._._._._._.-._._.-")
        return self.autonomia() - n_km

    @classmethod
    def cria_automovel(cls,cap,qtd,consumo):
        return cls(cap,qtd,consumo)