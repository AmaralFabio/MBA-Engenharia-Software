
let container = document.querySelector('.produtos');

// para cada produto na lista de produtos...
for (let produto of produtos) {
    // cria uma div
    let card = document.createElement('div');

    // adiciona a classe do css
    card.classList.add('card');

    // altera o conteúdo interno do card
    card.innerHTML = `
        <img src=${produto.imagem} alt="${produto.nome}">
        <h2>${produto.nome}</h2>
        <p>R$ ${produto.preco}</p>
        <button>Comprar</button>
    `;

    // adiciona o card ao container
    container.appendChild(card);
}

