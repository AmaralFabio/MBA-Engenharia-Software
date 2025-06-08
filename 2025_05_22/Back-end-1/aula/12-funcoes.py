produtos = [];  # lista para armazenar os produtos

def exibir_menu():
    print('\n=== Sistema de Cadastro de Produtos ===\n');
    print('1. Cadastrar Produto');
    print('2. Listar Produtos');
    print('3. Sair');

def cadastrar_produto(produtos):
    nome = input('Nome do produto: ')  # pede o nome do produto
    categoria = input('Categoria do produto: ');  # pede a categoria do produto
    preco = float(input('Preço do produto: '));  # pede o preço do produto

    produto = {
        'nome': nome,
        'categoria': categoria,
        'preco': preco
    };

    produtos.append(produto);  # adiciona o produto à lista

def listar_produtos(produtos):
    if not produtos:
        print('Nenhum produto cadastrado.');
        return;

    print('\n=== Lista de Produtos ===');
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. Nome: {produto['nome']} | Categoria: {produto['categoria']} | Preço: R${produto['preco']:.2f}");  # formata o preço com duas casas decimais
        
def sair():
    print('Saindo do sistema...');
    
def main():
    produtos = [];  # lista para armazenar os produtos

    while True:
        exibir_menu();  # exibe o menu
        opcao = input('Escolha uma opção: ');  # pede a opção ao usuário

        if opcao == '1':
            cadastrar_produto(produtos);  # chama a função para cadastrar produto
        elif opcao == '2':
            listar_produtos(produtos);  # chama a função para listar produtos
        elif opcao == '3':
            sair();  # chama a função para sair
            break;  # sai do loop
        else:
            print('Opção inválida. Tente novamente.');  # mensagem de erro para opção inválida

if __name__ == '__main__':
    main();  # chama a função principal para iniciar o programa 