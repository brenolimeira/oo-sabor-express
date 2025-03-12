from modelos.restaurante import Restaurante

restante_praca = Restaurante('praça', 'Gourmet')
restante_praca.receber_avaliacao('Gui', 10)
restante_praca.receber_avaliacao('Lais', 8)
restante_praca.receber_avaliacao('Emy', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__': 
    main()