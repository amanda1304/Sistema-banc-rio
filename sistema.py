menu = '''

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

=> '''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saque = 3

while True :

    opcao = input(menu)

    if opcao == 'd' :
        valor = float(input('informe o valor do depósito: ')) 

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor: .2f}\n'

        else:
            print('Operação falhou! o valor informado é inválido')

    elif opcao == 's' : 
        valor = float(input('informe o valor do saque: '))

        excedeu_saldo = valor > saldo            
        excedeu_limite = valor > limite  
        excedeu_saque = numero_saques >= limite_saque

        if excedeu_saldo:
            print('Operação falhou! você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Operação falhou! O valor de saque excede o limite.')

        elif excedeu_saque:
            print('O peração falhou! O número máximo de saque excedido')     
     
        elif valor > 0:
            saldo -= valor
            extrato += f'saque: R$ {valor: .2f}\n'
            numero_saques += 1

        else:
            print('Operação falhou! o valor informado é inválido')

    elif opcao == 'e':
        print('\n=============== Extrato===============')

        print('Não foram realizadas movimentações. ' if not extrato else extrato)
        print(f'\n saldo R$ {saldo: .2f}')

        print('\n======================================')

    elif opcao == 'q':
        break

    else:
       print('Operação inválida, por favor selecione novamente a operação desejada') 
