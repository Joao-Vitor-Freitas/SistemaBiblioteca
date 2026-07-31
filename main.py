import os

from Modelos.livro import Livro
from Modelos.biblioteca import Biblioteca


biblioteca = Biblioteca()


livro = Livro(
    "Devoradores de Estrelas",
    "Andy Weir",
    2021
)

print(livro)

livro.emprestar()

print(livro)

livro.emprestar()

livro.devolver()

livro.devolver()

biblioteca.adicionar(livro)


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


print("\n=== LIVROS DA BIBLIOTECA ===")
biblioteca.listar()


def iniciar():
    while True:

        limpar_tela()

        resposta_usuario = int(input("""
=========================
      Biblioteca
=========================

1 - Adicionar Livro

2 - Remover Livro

3 - Listar Livros

4 - Emprestar Livro

5 - Devolver Livro

0 - Sair

Escolha: """))

        try:

            match resposta_usuario:

                case 0:
                    print("\nSaindo...")
                    break

                case 1:
                    nome = input("Título: ")
                    autor = input("Autor: ")
                    ano = int(input("Ano: "))

                    livro = Livro(nome, autor, ano)
                    biblioteca.adicionar(livro)

                case 2:
                    biblioteca.remover_por_nome()

                case 3:
                    biblioteca.listar()

                case 4:
                    livro.emprestar()

                case 5:
                    livro.devolver()

                case _:
                    print("Opção inválida.")

        except ValueError:
            print("Digite um número válido.")


iniciar()