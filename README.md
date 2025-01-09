# Gerenciamento de Produtos

Este é um projeto em Python para gerenciar produtos em um inventário. O sistema permite adicionar, listar, atualizar, buscar e excluir produtos, com persistência de dados em um arquivo JSON.

## Funcionalidades

1. **Adicionar produto(s):** Adicione novos produtos ao inventário, incluindo ID, nome, categoria, quantidade e preço.
2. **Listar produtos:** Veja todos os produtos cadastrados no inventário em formato tabular.
3. **Atualizar produto(s):** Altere informações de um produto existente, como nome, categoria, quantidade ou preço.
4. **Buscar produto(s):** Pesquise um produto pelo ID ou por parte do nome.
5. **Excluir produto(s):** Remova um produto do inventário pelo ID.
6. **Persistência de dados:** Todos os dados são salvos no arquivo `produtos.json`.

## Tecnologias Utilizadas

- Python 3
- Biblioteca `json` (para manipulação do arquivo JSON)
- Biblioteca `os` (para verificar a existência do arquivo JSON)

## Como Executar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/gerenciamento-de-produtos.git
cd gerenciamento-de-produtos
```

### 2. Configurar o Ambiente

Certifique-se de ter o Python 3 instalado. Verifique a versão com:

```bash
python --version
```

### 3. Executar o Projeto

No diretório do projeto, execute o seguinte comando:

```bash
python main.py
```

### 4. Uso do Programa

Siga as instruções no menu para gerenciar os produtos no inventário.

## Estrutura do Projeto

```
.
├── main.py          # Arquivo principal do programa
├── produtos.json    # Arquivo de dados para persistência
├── README.md        # Documentação do projeto
```

## Exemplo de Uso

### Adicionar Produto

```text
*** Menu ***

1 - Adicione produto(s)
2 - Lista de produtos
3 - Atualizar produto(s)
4 - Buscar produto(s)
5 - Deletar produto(s)
6 - Sair do programa

Escolha uma opção: 1
Digite o nome do produto: Teclado
Digite a categoria do produto (ex: smartphones, laptops, acessórios): Acessórios
Digite a quantidade deste produto em estoque: 10
Digite o preço unitário deste produto: 120.50
Produto(s) adicionado(s) com sucesso!
```

### Listar Produtos

```text
*** Menu ***

Escolha uma opção: 2
ID   Nome                                    Categoria                               Quantidade Preço     
---------------------------------------------------------------------------------------------
1    Teclado                                 Acessórios                              10         120.50    
```

## Possíveis Melhorias Futuras

- Adicionar suporte a banco de dados (SQLite ou PostgreSQL).
- Implementar uma interface gráfica (GUI) para facilitar o uso.
- Criar testes automatizados para garantir a estabilidade do código.
- Adicionar controle de usuários e autenticação.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contribuições

Contribuições são bem-vindas! Para sugerir mudanças, crie um _fork_ do repositório, realize as alterações e envie um _pull request_.

