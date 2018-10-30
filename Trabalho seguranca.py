'''
[feito]Faça um programa que tenha cadastrado, preveamente, 10 descrições de risco

[feito]O usuário entrará com o IMPACTO e a PROBABILIDADE

[feito]Automaticamente o sistma gera o RISCO posteriormente o sitema abre os campo para
digitar as ações para mitigar o RISCO

[feito]A tabela completa deve ser mostrada na tela.
'''

#String da tabela de risco
tabelaDeRisco = '''
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

#Cria dicionários vazios paar armazenar os níveis de risco, ação para mitigar, probabilidade e impacot
risco = {}
mitigar = {}
probabilidade = {}
impacto = {}

#recebe o nível deimpacto e a probabilidade e retorna o nível de risco
def nivelRisco(impa, prob):
    if (impa == 1):
        if(prob == 5):
            return 'Médio'
        else:
            return 'Baixo'
    elif (impa == 2):
        if(prob == 1 or prob == 2):
            return 'Baixo'
        elif(prob == 5):
            return 'Alto '
        else:
            return 'Médio'
    elif (impa == 3):
        if (prob == 1):
            return 'Baixo'
        elif(prob == 2 or prob == 3):
            return 'Médio'
        else:
            return 'Alto '
    elif (impa == 4):
        if (prob == 1 or prob == 2):
            return 'Baixo'
        else:
            return 'Alto '
    elif (impa == 5):
        if (prob == 1 or prob == 2):
            return 'Médio'
        else:
            return 'Alto '

#Alimenta os dicionários
def tabelaRisco():
    for i in range(10):
        print(tabelaDeRisco)
        impa = int(input("Qual o impacto do risco \"{}\" ?\n" .format(riscos[i+1])))
        if(impa == 1):
            impacto[i+1] = 'Insignificante'
        elif(impa == 2):
            impacto[i+1] = 'Baixo         '
        elif(impa == 3):
            impacto[i+1] = 'Médio         '
        elif(impa == 4):
            impacto[i+1] = 'Alto          '
        else:
            impacto[i+1] = 'Trágico       '
        prob = int(input("Qual a Probabilidade do risco: \"{}\" ?\n" .format(riscos[i+1])))
        if(prob == 1):
            probabilidade[i+1] = 'Remota        '
        elif(prob == 2):
            probabilidade[i+1] = 'Baixa         '
        elif(prob == 3):
            probabilidade[i+1] = 'Média         '
        elif(prob == 4):
            probabilidade[i+1] = 'Alta          '
        else:
            probabilidade[i+1] = 'Elevadíssima  '
        risco[i+1] = nivelRisco(impa, prob)
        mitigar[i+1] = input("Digite a ação para mitigar o risco \"{}\" nível: {}\n".format(riscos[i+1], risco[i+1]))

#define qual a maior string para a cração da tabela final
def maior():
    maiorPalavra = ""
    for i in range(10):
        if(len(mitigar[i+1]) > len(maiorPalavra)):
            maiorPalavra = mitigar[i+1]
    return maiorPalavra

#Gera a tabela final
def montarTabela():
    maiorPalavra = maior()
    if(len(maiorPalavra) < 18):
        barra = '-' * 19
    else:
        barra = '-'*len(maiorPalavra)
        espaco = " " * (len(maiorPalavra) - 18)
    print('Ativo: Servidor de arquivos')
    print('+--------------------------+--------------+--------------+-----------------------+{}+'.format(barra))
    print('|Descrição do risco        |Impacto       |Probabilidade |Classificação de risco |Ação para mitigar{}|'.format(espaco))
    print('+--------------------------+--------------+--------------+-----------------------+{}+'.format(barra))
    print('|Infecção por vírus        |{}|{}|{}                  |{}{}|'.format(impacto[1], probabilidade[1], risco[1], mitigar[1], espaco))
    print('+--------------------------+--------------+--------------+-----------------------+{}+'.format(barra))
    print('|IAcesso indevido às pastas|{}|{}|{}                  |{}{}|'.format(impacto[2], probabilidade[2], risco[2], mitigar[2], espaco))
    print('+--------------------------+--------------+--------------+-----------------------+{}+'.format(barra))
    print('|Não realização de backup  |{}|{}|{}                  |{}{}|'.format(impacto[3], probabilidade[3], risco[3], mitigar[3], espaco))
    print('+--------------------------+--------------+--------------+-----------------------+{}+'.format(barra))
    print('|Arrombamento da sala      |{}|{}|{}                  |{}{}|'.format(impacto[4], probabilidade[4], risco[4], mitigar[4], espaco))
    print('+--------------------------+--------------+--------------+-----------------------+{}+'.format(barra))
    print('|Senhas fracas             |{}|{}|{}                  |{}{}|'.format(impacto[5], probabilidade[5], risco[5], mitigar[5], espaco))
    print('+--------------------------+--------------+--------------+-----------------------+{}+'.format(barra))
    print('|Incêndio                  |{}|{}|{}                  |{}{}|'.format(impacto[6], probabilidade[6], risco[6], mitigar[6], espaco))
    print('+--------------------------+--------------+--------------+-----------------------+{}+'.format(barra))
    print('|Queda de energia          |{}|{}|{}                  |{}{}|'.format(impacto[7], probabilidade[7], risco[7], mitigar[7], espaco))
    print('+--------------------------+--------------+--------------+-----------------------+{}+'.format(barra))
    print('|Desastre Natural          |{}|{}|{}                  |{}{}|'.format(impacto[8], probabilidade[8], risco[8], mitigar[8], espaco))
    print('+--------------------------+--------------+--------------+-----------------------+{}+'.format(barra))
    print('|Erro humano               |{}|{}|{}                  |{}{}|'.format(impacto[9], probabilidade[9], risco[9], mitigar[9], espaco))
    print('+--------------------------+--------------+--------------+-----------------------+{}+'.format(barra))
    print('|Falta de manutenção       |{}|{}|{}                  |{}{}|'.format(impacto[10], probabilidade[10], risco[10], mitigar[10], espaco))
    print('+--------------------------+--------------+--------------+-----------------------+{}+'.format(barra))


def main():
    tabelaRisco()
    montarTabela()
#Inicia o prigrama
main()
