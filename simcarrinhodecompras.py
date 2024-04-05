# Declaração de variáveis que serão utilizadas
carrinho = {}
escolha = 0
nomeproduto = str
valorproduto = 0
total = 0
# Estrutura de repetição para manipular o carrinho
while True:
    print('[1] Adicionar produto\n[2] Remover último produto\n[3] Revisar pedido'
          '\n[4] finalizar pedido')
    escolha = int(input('Sua escolha(APENAS NÚMEROS): '))
    if escolha == 1:
        nomeproduto = str(input('Digite o nome do produto: '))
        valorproduto = float(input('Digite o valor do produto: '))
        carrinho[nomeproduto] = valorproduto
        total += valorproduto
    if escolha == 2:
        print(f'{nomeproduto} removido(a) com sucesso.')
        carrinho.popitem()
        total -= valorproduto
    if escolha == 3:
        for chave in carrinho.keys():
            print(f'Produto: {chave}\nvalor: R${carrinho[chave]}')
            print('-' * 20)
        print(f'Total: R${total}')
    if escolha == 4:
        break
    if escolha < 1 and escolha >4:
        print('Opção inválida, tente novamente.')
# Estrutura de repetição para evitar bugs ao selecionar forma de pagamento.
while True:
    print('Como Deseja pagar?\n[1] Pagamento à vista ou cartão de débito(5% de desconto)\n'
      '[2] Em até 4x no cartão(sem juros)\n[3] Em 5x ou mais no cartão(10% de juros) ')
    escolhapag = int(input('Sua escolha(APENAS NÚMEROS): '))
    if escolhapag == 1:
        total *= 0.95
        break
    if escolhapag == 2:
        break
    if escolhapag == 3:
        total *= 1.10
        break
    if escolhapag != 1 and escolhapag != 2 and escolhapag != 3:
        print('Opção inválida, tente novamente.')
for chave in carrinho.keys():
    print(f'Produto: {chave}\nvalor: R${carrinho[chave]}')
    print('-' * 20)
print(f'Valor final: R${total}')