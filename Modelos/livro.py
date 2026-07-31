from Modelos.biblioteca import Biblioteca

class Livro:

    def __init__(self, nome, autor, ano):
        self._nome = nome.title()
        self._autor = autor
        self._ano = ano
        self._disponivel = True

    def __str__(self):
        return f'{self._nome} | {self._autor} | {self._ano} | {self._disponivel}'

    def emprestar(self):
        if self._disponivel:
            print(f'O livro "{self._nome}" está disponível para empréstimo.')
            self._disponivel = False
        else:
            print("Livro já está emprestado.")

    def devolver(self):
        if not self._disponivel:
            print(f'O livro "{self._nome}" foi devolvido.')
            self._disponivel = True
        else:
            print("O livro já estava disponível.")