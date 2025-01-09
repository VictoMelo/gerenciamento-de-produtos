import json
import os

ARQUIVO_DE_DADOS = "produtos.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_DE_DADOS):
        with open (ARQUIVO_DE_DADOS, "r") as arquivo:
            return json.load(arquivo)
        return[]

def salvar_dados(dados):
    with open(ARQUIVO_DE_DADOS, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

def gera_id(dados):
    return max ((produto["id"] for produto in dados), default=0) + 1

def menu ():
    while True:
        print("\n*** Menu ***") 
        print("\n1 - Adicione produto(s)")
        print("2 - Lista de produto")
        print("3 - Atualizar produto(s)")
        print("4 - Buscar produto(s) ")
        print("5 - Deletar produto(s)")
        print("6 - Sair do programa")
        
        try:
            opcao = int(input("\nEscolha uma opcao : "))
            if opcao <1 or opcao >6:
                raise ValueError
        except ValueError:
            print("Favor digite um numero válido. Opções de 1 à 6.")
            continue

        if opcao == 1:
            adicionar_produto()
        elif opcao == 2:
            lista_produto()
        elif opcao == 3:
            atualizar_produto()
        elif opcao == 4:
            buscar_produto()
        elif opcao == 5:
            deletar_produto()
        elif opcao == 6:
            print("Encerrando programa...")
            break



def adicionar_produto():
    dados = carregar_dados()
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto (ex: smartphones, laptops, acessórios): ")
    quantidade = int(input("Digite a quantidade deste produto em estoque: "))
    preco = float(input("Digite o preço unitário deste produto: "))
    novo_produto = {
        "id": gera_id(dados),
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco
    }
    dados.append(novo_produto)  
    salvar_dados(dados) 
    print("Produto(s) adicionado(s) com sucesso!")

def lista_produto():
    dados = carregar_dados()
    if not dados:
        print("O invertário está vazio.")
        return
    print(f"{'ID':<5}{'Nome':<40}{'Categoria':<40}{'Quantidade':<10}{'Preço':<5}")
    print("-" * 60)
    for produto in dados:
        print(f"{produto['id']:<5}{produto['nome']:<40}{produto['categoria']:<40}{produto['quantidade']:<10}{produto['preco']:<10.2f}")

def atualizar_produto():
    dados = carregar_dados()
    id_produto = int(input("Inform o ID do item que deseja atualizar: "))
    produto = next((p for p in dados if p["id"] == id_produto), None)
    if not produto:
        print("Produto não localizado no sistema")
        return
    print(f"Produto localizado {produto}")
    print("Caso não deseja alterar nada em um campo especifico, apenas deixe em branco.")
    nome = input ("Digite o novo nome do produto: ").strip() or produto["nome"]
    categoria = input ("Digite a nova categoria do produto: ").strip() or produto["categoria"]
    quantidade = input("Digite a nova quantidade deste produto em estoque: ").strip() 
    preco = input("Digito o novo preço unitário deste produto: ").strip()
    produto.update({"nome": nome, "categoria": categoria, "quantidade": int(quantidade), "preco":float(preco)})
    salvar_dados()
    print("O produto foi atualizado com sucesso !")

def buscar_produto():
    dados = carregar_dados()
    buscador = input("Digite o ID do produto ou parte do nome: ").strip()
    if buscador.isdigit():
        produto = next((b for b in dados if b["id"] == int(buscador)), None)
        if produto:
            print(produto)
        else:
            print("Produto não localizado no sistema.")
    else:
        encontrados = [b for b in dados if buscador.lower() in b["nome"].lower()]
        if encontrados:
            for b in encontrados:
                print(b)
        else:
            print("Nenhum produto localizado no sistema.")       
                         
def deletar_produto():
    dados = carregar_dados()     
    id_produto = int(input("Informe o ID do produto que deseja excluir: "))
    produto = next((p for p in dados if p["id"] == id_produto), None)
    if not produto:
        print("Produto não encontrado.")
        return
    confirm = input("Deseja realmente excluir o produto {produto['nome']} ? (s/n): ")
    if confirm.lower() == "s":
        dados = [p for p in dados if p["id"]!= id_produto]
        salvar_dados(dados)
        print("Produto foi excluido com sucesso !")  

if __name__ == "__main__":
    menu()