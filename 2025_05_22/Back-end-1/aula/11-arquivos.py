import json; # importa o módulo json para manipulação de arquivos JSON

produtos = [];

while True:
    nome = input('Nome do produto: '); # pede o nome do produto
    categoria = input('Categoria do produto: '); # pede a categoria do produto
    preco = float(input('Preço do produto: ')); # pede o preço do produto

    produtos.append({
        'nome': nome,
        'categoria': categoria,
        'preco': preco
    });

    continuar = input('Deseja cadastrar outro produto? (s/n): ').lower(); # pergunta se deseja cadastrar outro produto

    if continuar != 's': # se a resposta for diferente de 's'
        break;

with open('produtos.json', 'w', encoding='utf-8') as f: # abre o arquivo produtos.json para escrita
    json.dump(produtos, f, ensure_ascii=False, indent=4); # escreve cada produto no arquivo em formato JSON        

print('Produtos cadastrados com sucesso!'); # mensagem de sucesso ao cadastrar os produtos

# exibe os produtos cadastrados
print('\nProdutos cadastrados:');

for produto in produtos:
    print(f"Nome: {produto['nome']} | Categoria: {produto['categoria']} | Preço: R${produto['preco']:.2f}"); # formata o preço com duas casas decimais

# exibe o total de produtos cadastrados
print(f'Total de produtos cadastrados: {len(produtos)}'); # exibe o total de produtos cadastrados
