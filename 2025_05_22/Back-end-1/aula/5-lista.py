numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Lista original:', numeros);
print('Primeiro elemento:', numeros[0]);
print('Ultimo elemento:', numeros[-1]);

# Adicionando um elemento ao final da lista
numeros.append(11);

print('Nova lista original:', numeros);

# Removendo um elemento da lista
numeros.remove(5);

print('Lista apos remover o 5:', numeros);

# para cada número na lista
for numero in numeros:
    print('Número:', numero);

print('Verificando se um elemento está na lista');
carros = ['Fusca', 'Civic', 'Corolla', 'Onix'];

# se 'Civic' está na lista de carros
if 'Uno' in carros:
    print('Uno está na lista de carros');
else:
    print('Uno não está na lista de carros');
    for carro in carros:
        print('Carro:', carro);