'''
[feito]Faça um programa que tenha cadastrado, preveamente, 10 descrições de risco

O usuário entrará com o IMPACTO e a PROBABILIDADE

Automaticamente o sistma gera o RISCO posteriormente o sitema o campo para
digitar as ações para mitigar o RISCO

A tabela completa deve ser mostrada na tela.
'''


tabelaRisco = '''
Tabela de Risco
+-------------+---------+------+------+------+---------+
|Impacto      | 1       |2     |3     |4     | 5       |
+-------------+---------+------+------+------+---------+
|Probabilidade|                                        |
+-------------+---------+------+------+-------+--------+
|1            |Baixo    |Baixo |Baixo |Baixo  |Médio   |
+-------------+---------+------+------+-------+--------+
|2            |Baixo    |Baixo |Médio |Baixo  |Médio   |
+-------------+---------+------+------+-------+--------+
|3            |Baixo    |Médio |Médio |Alto   |Alto    |
+-------------+---------+------+------+-------+--------+
|4            |Baixo    |Médio |Alto  |Alto   |Alto    |
+-------------+---------+------+------+-------+--------+
|5            |Médio    |Alto  |Alto  |Alto   |Alto    |
+-------------+---------+------+------+-------+--------+
Legenda
Probabilidade: Remota = 1, baixa = 2, média = 3, alta = 4, elevadíssima = 5
Impacto: Insignificante = 1, baixo = 2, médio = 3, alto = 4, trágico = 5
'''
riscos = {1:'Infecção por vírus', 2:'Acesso indevido às pastas',
3:'Não realização de bacup', 4:'Arrombamnto da Sala',
5:'Senhas fracas', 6:'incêndio', 7:'Queda de energia',
8:'Desastre natural', 9:'Erro humano', 10:'Falta de manutenção'}

#Cria um dicionário vazio paar armazenar os níveis de rosco
risco = {}

def nivelRisco(impa, prob):
    if (impa == 1):
        if(prob == 5):
            return 'Médio'
        else:
            return 'Baixo'
    elif (impa == 2):
        if(prob == 1 | prob == 2):
            return 'Baixo'
        elif(prob == 5):
            return 'Alto'
        else:
            return 'Médio'
    elif (impa == 3):
        if (prob == 1):
            return 'Baixo'
        elif(prob == 2 | prob == 3):
            return 'Médio'
        else:
            return 'Alto'
    elif (impa == 4):
        if (prob == 1 | prob == 2):
            return 'Baixo'
        else:
            return 'Alto'
    elif (impa == 5):
        if (prob == 1 | prob == 2):
            return 'Médio'
        else:
            return 'Alto'

def tabelaRisco():
    for i in range(2):
        impa = int(input("Qual o impacto do risco \"{}\" ?\n" .format(riscos[i+1])))
        prob = int(input("Qual a Probabilidade do risco: \"{}\" ?\n" .format(riscos[i+1])))
        risco[i+1] = nivelRisco(impa, prob)

def main():
    tabelaRisco()
    for i in range(2):
        print(risco[i+1])

main()
