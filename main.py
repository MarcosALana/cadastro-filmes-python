# Dia 9 - Cadastro de Filmes Favoritos

generos = ("Ação", "Comédia", "Drama", "Ficção", "Terror")
assistidos = set()

print("=== Cadastro de Filmes ===")
print("Gêneros disponíveis:", generos)

while True:
    print("\n1 - Adicionar filme assistido")
    print("2 - Ver filmes assistidos")
    print("3 - Ver novos lançamentos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        filme = input("Digite o nome do filme: ")
        assistidos.add(filme)  # set evita duplicados
        print(f"{filme} adicionado com sucesso!")
    elif opcao == "2":
        if assistidos:
            print("\n=== Filmes assistidos ===")
            for filme in assistidos:
                print("-", filme)
        else:
            print("Nenhum filme cadastrado ainda.")
    elif opcao == "3":
        novos = {"Duna 2", "Barbie", "Oppenheimer", "Avatar 2"}
        sugestao = novos - assistidos
        print("\n=== Novos lançamentos ainda não assistidos ===")
        for filme in sugestao:
            print("-", filme)
    elif opcao == "0":
        print("Encerrando programa. Até logo!")
        break
    else:
        print("Opção inválida.")
