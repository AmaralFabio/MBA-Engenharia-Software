import { exibirProdutos } from "./showProducts.js";

export function ativarBusca(listaDeProdutos) {
    let input = document.getElementById("searchInput");
    
    input.addEventListener("input", (event) => {

        let busca = event.target.value.toLowerCase();

        let produtosFiltrados = listaDeProdutos.filter(produto => {
            return produto.nome.toLowerCase().includes(busca);
        });

        exibirProdutos(produtosFiltrados);
    });
}