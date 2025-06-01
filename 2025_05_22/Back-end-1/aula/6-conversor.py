# crio a variável taxa_dolar
taxa_dolar = 5.72;

# Solicito ao usuário o valor em reais
valor_real = input('Digite o valor em reais (R$): ');

# realiza o cambio
resultado = float(valor_real) / taxa_dolar;

# Exibe o resultado
print(f'O valor em dólares (US$) é: {resultado:f}');

