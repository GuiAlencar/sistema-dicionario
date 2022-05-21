perguntas = {
    'Pergunta 1' : {
        'pergunta' : 'quanto é 2 + 2 ?',
        'respostas': { 'a' : '1', 'b' : '4', 'c' : '5',},
        'resposta_certa' : 'b',
    },
       'Pergunta 2' : {
        'pergunta' : 'quanto é 3 * 2 ?',
        'respostas': { 'a' : '4', 'b' : '10', 'c' : '6',},
        'resposta_certa' : 'c',
    },
}

print()
respostas_certas = 0
for chave, valor in perguntas.items():
    print(f'{chave}: {valor["pergunta"]}')

    print('Resposta: ')
    for chave_resposta, valor_reposta in valor['respostas'].items():
        print(f'[{chave_resposta}]: {valor_reposta}')
    
    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == valor['resposta_certa']:
        print('Você acertou!!')
        respostas_certas += 1
    else:
        print('Você errou!!')

print()
print()
qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100
print(f"Você acertou {respostas_certas} perguntas!! ")
print(f"Sua porcentagem de acerto foi de {porcentagem_acerto}%")

