from biblioteca import*
'''
Lista de Exercícios referentes a estruturas de iteração (repetição)
'''
def exemploPara():
    for x in range(10):# vai de 0 a 9
        print(x, end= ' ')
    for x in range(1,11): # vai de 1 a 10
        print(x, end= ' ')
    for x in range(1,50,2): # vai de 1 a 49 pulando de 2 em 2
        print(x, end= ' ')

def exemploEnquanto():
    x = 0 
    while x < 10:
        break #interromper a execução do laço
        x+= 1
        if x == 3:
            continue #salta para a próxima iteração
            print(x)
        else:
                print('Fim!')#nunca é executado, já que x nunca é >= 10
#1.Faça um programa que imprima todos os números de 1 até 200.
def q1():
    for x in range(1,201): #vai de 1 a 201
        print(x,end=' ')
#2. Faça um programa que imprima todos os números pares de 100 até 1.
def q2():
    for x in range(100,0,-2):
        print(x, end=' ')
#3. Faça um programa que imprima os múltiplos de 5, no intervalo de 1 até 500.
def q3():
    for x in range(0,501,5):
        print(x, end=' ')
#4. Faça um programa que permita entrar com o nome, a idade e o sexo de 20
#pessoas.O programa deve imprimir o nome da pessoa se ela for do sexo masculino
#e tiver mais de 21 anos e se for feminino .
def q4():
    for x in range(3):
        nome = input('Nome: ')
        sexo = input('Sexo: ').upper()[0]
        idade = int(input('Idade: '))
        if sexo == 'M' and idade >= 21:
            print(f'{nome} é do sexo masculino e maior de 21.' )
#5. Sabendo-se que a unidade lógica e aritmética calcula o produto através de somas
#sucessivas, crie um programa que calcule o produto de dois números inteiros
#lidos. Suponha que os números lidos sejam positivos.
def q5():
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))
    resultado = 0
    for _ in range(num1):
        resultado = resultado + num2
    print(resultado)
#6. Crie um programa que imprima os 20 primeiros termos da série de Fibonacci.
#Observação: os dois primeiros termos desta série são 1 e 1 e os demais são gerados
#a partir da soma dos anteriores. Exemplo:
#• 1 + 1 = 2, terceiro termo;
#• 1 + 2 = 3, quarto termo, etc.
# 1 1 2 3 5 8 13 21
def q6():
    ant = 1
    atu = 1
    print(ant, end=' ' )
    print(atu, end=' ' )
    for _ in range(18):
        pro = ant + atu        
        print(pro, end=' ')
        ant = atu
        atu = pro

#7. Crie um programa que permita entrar com o nome, a nota da
#prova 1 e da prova 2 de 15 alunos. Ao final, imprimir uma listagem, contendo:
#nome, nota da prova 1, nota da prova 2, e média das notas de cada aluno. Ao final,
#imprimir a média geral da turma.
def q7():
    resultado = ' '
    media_geral = 0
    for _ in range(3):
        nome = input(' Nome: ')
        n1 = float(input(' Nota1: '))
        n2 = float(input(' Nota2: '))
        media = round((n1+n2)/2,1)
        media_geral+= media
        resultado += f'{nome}\t{n1}\t{n2}\t{media}\n'
    print(' Nome\tN1\tN2\tMedia')
    print(resultado)
    print(f'Media da Turma: {round(media_geral/3,1)} ')

#8. Faça um programa que permita entrar com o nome e o salário bruto de 10 pessoas.
#Após ler os dados, imprimir o nome e o valor da alíquota do imposto de renda
#calculado conforme a tabela a seguir:
#Salário IRRF
#Salário menor que R$1300,00 Isento
#Salário maior ou igual a R$1300,00 e menor que R$2300,00 10% do salário bruto
#Salário maior ou igual a R$2300,00 15% do salário bruto
def q8():
    resultado = ' '
    for _ in range(3):
        nome = input('Nome: ')
        salario = float(input('salário: R$ '))
        irpf = salario * (0 if salario < 1300 else 0.10 if salario < 2300 else 0.15)
        resultado += f'{nome}\t{salario}\t{round(irpf, 2)}\n'
    print('Nome\tsalario(R$)\tirpf(R$)')
    print(resultado)
        


#9. No dia da estreia do filme "Procurando Dory", uma grande emissora de TV realizou
#uma pesquisa logo após o encerramento do filme. Cada espectador respondeu
#a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
#excelente - 3; bom - 2; regular - 1. Criar um programa que receba a idade e a
#opinião de 20 espectadores, calcule e imprima:
#• A média das idades das pessoas que responderam excelente;
#• A quantidade de pessoas que responderam regular;
#• A percentagem de pessoas que responderam bom entre todos os expectadores
#analisados.



#10. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
#que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
#jogadores, crie um programa que apresente as seguintes informações:
#
#• O peso médio e a idade média de cada um dos times;
#• O atleta mais pesado de cada time;
#• O atleta mais jovem de cada time;
#• O peso médio e a idade média de todos os participantes.
    
#11. Construa um programa que leia vários números e informe quantos números
#entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido, o algoritmo
#deverá cessar sua execução.
def q11():
    num = -1
    contador = 0
    while num != 0:
        num = int(input(' Digite um número: '))
        if num >= 100 and num <= 200:
            contador += 1
    print(f' Quantidade de valores entre 100 e 200: {contador}')

#12. Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
#ano, e um país B com 7 milhões de habitantes e uma taxa de natalidade de 2% ao
#ano, fazer um programa que calcule e imprima o tempo necessário para que a
#população do país A ultrapasse a população do país B.
def q12():
    populacaoA = 5_000_000
    populacaoB = 7_000_000
    anos = 0
    while populacaoA  <  populacaoB:   
        anos+=
        populacaoA += populacaoA*0.03
        populacaoB += populacaoB*0.02
    print(f' Após {anos} anos: ')
    print(f' Populacao A = {populacaoA}')
    print(f' Populacao B = {populacaoB}')

#13. Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores
#de consumo. Para cada consumidor, são digitados os seguintes dados:
#• número do consumidor
#• quantidade de kWh consumidos durante o mês
#• tipo (código) do consumidor
#1-residencial, preço em reais por kWh = 0,3
#2-comercial, preço em reais por kWh = 0,5
#3-industrial, preço em reais por kWh = 0,7
#Os dados devem ser lidos até que seja encontrado o consumidor com número 0
#(zero). O programa deve calcular e imprimir:
#• O custo total para cada consumidor
#• O total de consumo para os três tipos de consumidor
#• A média de consumo dos tipos 1 e 2
def q13():
    numero = -1
    consumo_geral = 0
    consumo_tipo = 0
    qtde_tipo_1_2 = 0
    while numero != 0:
        custo = 0
        numero = input_int('Número do Consumo: ',0,9_999_999)
        if numero == 0:
            break
        qtd_kw = input_int('Qtde de Kwh:',9_9999_999)
        tipo = input_int('Tipo do Consumidor:',1,3)
        custo += qtd_Kw * 0.3 if tipo == 1 else 0;
        custo += qtd_Kw * 0.5 if tipo == 2 else 0;
        custo += qtd_Kw * 0.7 if tipo == 3 else 0;
        consumo_tip_1_2 += qtd_kw if tipo == 1 else 0;
        consumo_tip_1_2 += qtd_kw if tipo == 2 else 0;
        qtde_tipo_1_2 += 1 if tipo == 1 else 0;
        qtde_tipo_1_2 += 1 if tipo == 2 else 0;
        print(f'Custo total do consumidor: R$ {custo}')
    print(f'Consumo Geral: {consumo_geral} Kw')
    print(f'Média de consumo tipo 1 e 2: {consumo_tipo_1 e 2/qtde_tipo_1_2} Kwh')


#14. Faça um programa que leia vários números inteiros e apresente o fatorial de cada
#número. O algoritmo encerra quando se digita um número menor do que 1.

#15. Faça um programa que permita entrar com a idade de várias pessoas e
#imprima:
#• total de pessoas com menos de 21 anos
#• total de pessoas com mais de 50 anos
def 15():
    menos_de_21 = 0
    mais_de_50 = 0
    while true:
        try:
            idade = int(input('Digite a idade(ou 0 para sair): '))
            if idade == 0:
                break
                if idade < 21:
                    menos_de_21 += 1
                if idade > 50:
                    mais_de_50 += 1
    expect ValueError:
            print('Entrada inválida! Por favor, digite um número válido.')
    print('\nResultados: ')
    print(f' Total de pessoas com menos de 21 anos: {menos_de_21}')
    print(f' Total de pessoas com mais de 50 anos: {mais_de_50}')
if __name__ == "__main__":
    main()




#16. Sabendo-se que a unidade lógica e aritmética calcula a divisão por meio de subtrações
#sucessivas, criar um algoritmo que calcule e imprima o resto da divisão de
#números inteiros lidos. Para isso, basta subtrair o divisor ao dividendo, sucessivamente,
#até que o resultado seja menor do que o divisor. O número de subtrações
#realizadas corresponde ao quociente inteiro e o valor restante da subtração corresponde
#ao resto. Suponha que os números lidos sejam positivos e que o dividendo
#seja maior do que o divisor.
#Exemplo:
#  10 / 5
#  10 é o Dividendo
#  5 é o Divisor
#  2 é o Quociente (resultado inteiro da divisão)
#  0 é o Resto da Divisão

#17. Crie um programa que possa ler um conjunto de pedidos de compra e
#calcule o valor total da compra. Cada pedido é composto pelos seguintes campos:
#• número de pedido
#• data do pedido (dia, mês, ano)
#• preço unitário
#• quantidade
#O programa deverá processar novos pedidos até que o usuário digite 0 (zero)
#como número do pedido.

#18. Uma pousada estipulou o preço para a diária em R$30,00 e mais uma taxa de
#serviços diários de:
#• R$15,00, se o número de dias for menor que 10;
#• R$8,00, se o número de dias for maior ou igual a 10;
#Faça um programa que imprima o nome, a conta e o número da conta de cada
#cliente e ao final o total faturado pela pousada.
#O programa deverá ler novos clientes até que o usuário digite 0 (zero) como
#número da conta.

#19. Em uma Universidade, os alunos das turmas de informática fizeram uma prova
#de algoritmos. Cada turma possui um número de alunos. Criar um programa que
#imprima:
#• quantidade de alunos aprovados;
#• média de cada turma;
#• percentual de reprovados.
#Obs.: Considere aprovado com nota >= 7.0

#20. Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas:
#• Qual o seu time de coração?
#1-Fluminense;
#2-Botafogo;
#3-Vasco;
#4-Flamengo;
#5-Outros
#• Onde você mora?
#1-RJ;
#2-Niterói;
#3-Outros
#• Qual o seu salário?
#Faça um programa que imprima:
#• o número de torcedores por clube;
#• a média salarial dos torcedores do Botafogo;
#• o número de pessoas moradoras do Rio de Janeiro, torcedores de outros
#clubes;
#• o número de pessoas de Niterói torcedoras do Fluminense
#Obs.: O programa encerra quando se digita 0 para o time.

#21. Em uma universidade cada aluno possui os seguintes dados:
#• Renda pessoal;
#• Renda familiar;
#• Total gasto com alimentação;
#• Total gasto com outras despesas;
#Faça um programa que imprima a porcentagem dos alunos que gasta acima de
#R$200,00 com outras despesas. O número de alunos com renda pessoal maior
#que a renda familiar e a porcentagem gasta com alimentação e outras despesas
#em relação às rendas pessoal e familiar.
#Obs.: O programa encerra quando se digita 0 para a renda pessoal.

#22. Crie um programa que ajude o DETRAN a saber o total de recursos que foram
#arrecadados com a aplicação de multas de trânsito.
#O algoritmo deve ler as seguintes informações para cada motorista:
#• número da carteira de motorista (de 1 a 4327);
#• número de multas;
#• valor de cada uma das multas.
#Deve ser impresso o valor da dívida para cada motorista e ao final da leitura o
#total de recursos arrecadados (somatório de todas as multas). O programa deverá
#imprimir também o número da carteira do motorista que obteve o maior número
#de multas.
#Obs.: O programa encerra ao ler a carteira de motorista de valor 0.

#23. Crie um programa que leia um conjunto de informações (nome, sexo, idade, peso
#e altura) dos atletas que participaram de uma olimpíada, e informar:
#• a atleta do sexo feminino mais alta;
#• o atleta do sexo masculino mais pesado;
#• a média de idade dos atletas.
#Obs.: Deverão se lidos dados dos atletas até que seja digitado o nome @ para um
#atleta.
#Para resolver este exercício, consulte a aula 7 que aborda o tratamento de strings,
#como comparação e atribuição de textos.

#24. Faça um programa que calcule quantos litros de gasolina são usados em uma
#viagem, sabendo que um carro faz 10 km/litro. O usuário fornecerá a velocidade
#do carro e o período de tempo que viaja nesta velocidade para cada trecho do
#percurso. Então, usando as fórmulas distância = tempo x velocidade e litros
#consumidos = distância / 10, o programa computará, para todos os valores não negativos
#de velocidade, os litros de combustível consumidos. O programa deverá
#imprimir a distância e o número de litros de combustível gastos naquele trecho.
#Deverá imprimir também o total de litros gastos na viagem. O programa encerra
#quando o usuário informar um valor negativo de velocidade.
#74 Aula 3. Estruturas de Iteração

#25. Faça um programa que calcule o imposto de renda de um grupo de contribuintes,
#considerando que:
#a) os dados de cada contribuinte (CIC, número de dependentes e renda bruta
#anual) serão fornecidos pelo usuário via teclado;
#b) para cada contribuinte será feito um abatimento de R$600 por dependente;
#c) a renda líquida é obtida diminuindo-se o abatimento com os dependentes
#da renda bruta anual;
#d) para saber quanto o contribuinte deve pagar de imposto, utiliza-se a tabela
#a seguir:
#Renda Líquida Imposto
#até R$1000 Isento
#de R$1001 a R$5000 15%
#acima de R$5000 25%
#e) o valor de CIC igual a zero indica final de dados;
#f ) o programa deverá imprimir, para cada contribuinte, o número do CIC e o
#imposto a ser pago;
#g) ao final o programa deverá imprimir o total do imposto arrecadado pela
#Receita Federal e o número de contribuintes isentos;
#h) leve em consideração o fato de o primeiro CIC informado poder ser zero.

#26. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma
#certa cidade, em um determinado dia. Para cada casa visitada foram fornecidos o
#número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo a ele
#naquela casa. Se a televisão estivesse desligada, nada seria anotado, ou seja, esta
#casa não entraria na pesquisa. Criar um programa que:
#• Leia um número indeterminado de dados, isto é, o número do canal e o
#número de pessoas que estavam assistindo;
#• Calcule e imprima a porcentagem de audiência em cada canal.
#Obs.: Para encerrar a entrada de dados, digite o número do canal zero.

#27. Crie um programa que calcule e imprima o CR do período para os alunos de
#computação. Para cada aluno, o algoritmo deverá ler:
#• número da matrícula;
#• quantidade de disciplinas cursadas;
#• notas em cada disciplina;
#Além do CR de cada aluno, o programa deve imprimir o melhor CR dos
#alunos que cursaram 5 ou mais disciplinas.
#• fim da entrada de dados é marcada por uma matrícula inválida (matrículas
#válidas de 1 a 5000);
#• CR do aluno é igual à média aritmética de suas notas.

#28. Construa um programa que receba a idade, a altura e o peso de várias pessoas,
#Calcule e imprima:
#• a quantidade de pessoas com idade superior a 50 anos;
#• a média das alturas das pessoas com idade entre 10 e 20 anos;
#• a porcentagem de pessoas com peso inferior a 40 quilos entre todas as
#pessoas analisadas.

#29. Construa um programa que receba o valor e o código de várias mercadorias
#vendidas em um determinado dia. Os códigos obedecem a lista a seguir:
#L-limpeza
#A-Alimentação
#H-Higiene
#Calcule e imprima:
#• o total vendido naquele dia, com todos os códigos juntos;
#• o total vendido naquele dia em cada um dos códigos.
#Obs.: Para encerrar a entrada de dados, digite o valor da mercadoria zero.

#30. Faça um programa que receba a idade e o estado civil (C-casado, S-solteiro, V-viúvo
#e D-desquitado ou separado) de várias pessoas. Calcule e imprima:
#• a quantidade de pessoas casadas;
#• a quantidade de pessoas solteiras;
#• a média das idades das pessoas viúvas;
#• a porcentagem de pessoas desquitadas ou separadas dentre todas as pessoas
#analisadas.
#Obs.: Para encerrar a entrada de dados, digite um número menor que zero para a
#idade.

questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')
