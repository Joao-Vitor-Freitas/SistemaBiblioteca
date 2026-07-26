from Modelos.livro import Livro
from Modelos.biblioteca import Biblioteca

livro = Livro("Devoradores de estrelas", "Andy Weir", 2021)

print(livro)

livro.emprestar()

print(livro)

livro.emprestar()

livro.devolver()

livro.devolver()


print("𝗕𝗲𝗺 𝘃𝗶𝗻𝗱𝗼 𝗮 𝗕𝗶𝗯𝗹𝗶𝗼𝘁𝗲𝗰𝗮❗")

def inicio():
        while True:
             
            print("𝗕𝗲𝗺 𝘃𝗶𝗻𝗱𝗼 𝗮 𝗕𝗶𝗯𝗹𝗶𝗼𝘁𝗲𝗰𝗮❗")
            pergunta = str(input("Você deseja adicionar um livro na biblioteca?(s/n)"))
            try:
                if pergunta != "s" and pergunta != "n":
                    print("Erro inesperado.")
                elif pergunta == "s":
                    #por que eu não consigo chamar a função adicionar da biblioteca, será que eu errei o import?
                    adicionar(livro)
                elif pergunta == "n":
                     break
                    
            except:
                return "Erro inesperado."