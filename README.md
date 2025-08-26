# Cadastro de Filmes em Python

Programa em Python que simula um **cadastro de filmes assistidos**.  
Usa **tupla** para representar gêneros disponíveis (imutáveis) e **set** para armazenar filmes já assistidos (sem repetição).

## 🚀 Código principal
```python
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
        assistidos.add(filme)
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


O que foi aprendido
Diferença entre listas, tuplas e conjuntos.
Uso de tupla para dados fixos (gêneros).
Uso de set para armazenar itens sem duplicação.
Operações de conjuntos: união, interseção e diferença.
Integração em um programa prático de cadastro.

💭 Comentário pessoal

Foi interessante aprender sobre tuplas e conjuntos.
Percebi que cada estrutura de dados tem uma função específica.
Gostei de usar set porque ele elimina duplicados automaticamente, algo muito útil em programas reais.
