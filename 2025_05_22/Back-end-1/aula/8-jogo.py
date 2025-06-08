import random;

numero_secreto = random.randint(1, 1000); # gera um número aleatório entre 1 e 10
tentativas = 0;

# enquanto não acertar...
while True:    
    chute = int(input('Digite um número entre 1 e 1000: ')); # pede um número ao usuário
    tentativas += 1; # incrementa o número de tentativas
    if chute == numero_secreto: # se o número for igual ao número secreto        
        break; # sai do loop
    elif chute < numero_secreto: # se o número for menor que o número secreto
        print('O número é maior!'); # informa que o número é maior
    else: # se o número for maior que o número secreto
        print('O número é menor!'); # informa que o número é menor

print(f'Parabéns! Você acertou o {numero_secreto} quer era o número secreto com {tentativas} tentativas!'); # exibe mensagem de fim de jogo