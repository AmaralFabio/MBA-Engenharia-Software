import { carregarProdutos } from "./productService.js";
import { ativarBusca } from "./searchProducts.js";
import { exibirProdutos } from "./showProducts.js";

async function main() {
    
    console.log("Iniciando a aplicação");

    // carregar os produtos
    let produtos = await carregarProdutos();

    // função para exibir os produtos na tela
    exibirProdutos(produtos);

    // buscar produtos
    ativarBusca(produtos);
}

main();