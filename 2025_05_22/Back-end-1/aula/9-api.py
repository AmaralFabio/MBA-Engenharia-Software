import requests;

response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL').json();

# print(response);

taxa_dolar = float(response['USDBRL']['bid']); # pega a cotação do dólar

print(f'Taxa do dólar: {taxa_dolar}'); # exibe a cotação do dólar

valor_em_real = float(input('Digite um valor em reais (R$): ')); # pede um valor em reais ao usuário

valor_em_dolar = valor_em_real / taxa_dolar; # converte o valor em reais para dólares

print(f'Valor em dólares (USD): {valor_em_dolar:.2f}'); # exibe o valor em dólares com duas casas decimais