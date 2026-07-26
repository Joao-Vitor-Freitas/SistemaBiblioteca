from Modelos.livro import Livro
class Biblioteca:
    _livros = []
    
    
    def adicionar(self, livro):
        self._livros.append(livro)
    

    

    def remover(self, livro):
        # pensar em como vou dar a opção de escolher na lista de livros
        x = input("Qual livro você deseja remover:")
        self.listar(livro)
        self._livros.remove(livro)
        self.listar()
    
    @classmethod
    def listar(cls):
        # acho que vou tirar esse classmethod e colocar como uma função simples com objeto tipo o adicionar
        print(f'{'Nome do livro'.ljust(25)} | {'Autor'.ljust(25)} | {'Ano'.ljust(25)} | {'Disponibilidade'}')
        for livro in cls._livros:    
            print(f'{livro._nome.ljust(25)} | {livro._autor.ljust(25)} | {livro._ano.ljust(25)}')

    