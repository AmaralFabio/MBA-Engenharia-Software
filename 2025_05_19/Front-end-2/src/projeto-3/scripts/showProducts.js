export async function exibirProdutos(listaDeProdutos) {

    let container = document.querySelector(".produtos");

    container.innerHTML = ""; // limpa o container antes de exibir os produtos

    // se não houver produtos, exibe uma mensagem
    if (listaDeProdutos.length <= 0) {
        container.innerHTML = "<p>Nenhum produto encontrado.</p>";        
        return;
    }

    for (let produto of listaDeProdutos) {
        let card = document.createElement("div");
        card.classList.add('card');
        card.innerHTML = `
            <img src="${produto.imagem}" alt="${produto.nome}">
            <h3>${produto.nome}</h3>
            <p>R$ ${produto.preco.toFixed(2)}</p>
            <button class="btn-comprar">Comprar</button>
        `;
        container.appendChild(card);
    }
}