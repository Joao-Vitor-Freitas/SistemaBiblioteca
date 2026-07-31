from Modelos.livro import Livro


class Biblioteca:

    def __init__(self):
        self._livros = []

    def adicionar(self, livro):
        self._livros.append(livro)

    def remover(self, livro):
        if livro in self._livros:
            self._livros.remove(livro)
            print("Livro removido com sucesso.")
        else:
            print("Livro não encontrado.")

    def remover_por_nome(self):
        encontrou = False
        excluir = input("Qual livro você deseja remover? ")

        for livro in self._livros:
            if (
                excluir == livro._nome
                or excluir == livro._autor
                or excluir == str(livro._ano)
            ):
                self.remover(livro)
                encontrou = True
                break

        if not encontrou:
            print("A biblioteca não possui este livro.")

    def listar(self):
        print(
            f'{"Nome do livro".ljust(25)} | '
            f'{"Autor".ljust(25)} | '
            f'{"Ano".ljust(10)} | '
            f'{"Disponível"}'
        )

        print("-" * 80)

        for livro in self._livros:
            print(
                f'{livro._nome.ljust(25)} | '
                f'{livro._autor.ljust(25)} | '
                f'{str(livro._ano).ljust(10)} | '
                f'{livro._disponivel}'
            )