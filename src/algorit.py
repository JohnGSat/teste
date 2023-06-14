vendas= int(input('Digite aqui o numero de vendas do mês ==>'))
dev=str(input('digite a data de desenvolvimento ==>'))
devtime=str(input('digite o horario do desenvolvimento ==>'))
valor=600+(vendas*5)+50

if(dev!='14/06/2023'):
    if(devtime!='15:54'):
        print('Errado essa atividade foi feita no dia 14/06/2023 no horario 15:54')


else:
    print('Correto! Essa atividade foi feita no dia 14/06/2023 no horario 15:54')
if(vendas==0):
    valor=valor-50
print('o salario total do(a) funcionario(a) foi de ',valor)