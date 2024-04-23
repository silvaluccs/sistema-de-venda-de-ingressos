'''
Autor: Lucas Oliveira da Silva
Componente Curricular: MI Algoritmos
Concluido em: 21/04/2024
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''



# variáveis para configuração do sistema
print()
print("#"*50)

print("\n\tConfigurações iniciais para o sistema.")

ingressos_disponiveis = int(input("\n\tDigite o número máximo de pessoas no evento: "))

parar_sistema = False

vendedor_padrao = input("\n\tDigite o vendedor oficial: ")
vendedor_convidado1 = input("\n\tDigite o primeiro vendedor convidado: ")
vendedor_convidado2 = input("\n\tDigite o segundo vendedor convidado: ")
numero_vendas_para_comissao = int(input("\n\tDigite o números de vendas para ganhar uma comissão: "))

valor_inteira = float(input("\n\tDigite o valor da inteira: R$"))
valor_meia = round(valor_inteira/2, 2) 
valor_ecomp = float(input("\n\tDigite o valor para estudantes de ECOMP: R$"))
valor_DA = 0

print()
print("#"*50)


# variáveis para salvar dados
soma_idades = 0


valor_arrecadado_inteira = 0
valor_arrecadado_meia = 0
valor_arrecadado_ecomp = 0
valor_arrecadado_DA_convidados = 0

numero_ingressos = ingressos_disponiveis # para salvar o número inicial de ingressos disponíveis
ingressos_inteira_vendidos = 0
ingressos_ecomp_vendidos = 0
ingressos_estudante_vendidos = 0
ingressos_idosos_vendidos = 0
ingressos_DA_vendidos = 0
ingressos_convidados_vendidos = 0

ingressos_vendedor_padrao = 0
ingressos_vendedor1 = 0
ingressos_vendedor2 = 0

comissoes_vendedor1 = 0
comissoes_vendedor2 = 0


#fluxo prinicpal:
print("\n\n\tIniciando vendas: ")
while (ingressos_disponiveis > 0) and (not parar_sistema):

    nome = input("\n\n\tDigite o nome do comprador: ")
    idade = input("\tDigite a idade do comprador: ")
    idade = int(idade)
    soma_idades += idade


# Selecionar o tipo de vendedor
    escolha_vendedor = False
    while not escolha_vendedor:
        print("\n\tSelecione o vendedor:")
        print(f"\t1. {vendedor_padrao}\n\t2. {vendedor_convidado1}\n\t3. {vendedor_convidado2}")
        vendedor = input("\n\tEscolha(número): ")

        if vendedor == "1":
            ingressos_vendedor_padrao += 1
            escolha_vendedor = True

        elif vendedor == "2":
            ingressos_vendedor1 += 1
            escolha_vendedor = True

        elif vendedor == "3":
            ingressos_vendedor2 += 1
            escolha_vendedor = True
        
        else:
            print("\n\tPor favor, selecione um vendedor oficial.")



# Selecionar o tipo de ingresso

    ingresso_inteira = False
    ingresso_meia = False
    ingresso_meia_idoso = False
    ingreso_meia_estudante = False
    ingresso_ecomp = False
    ingresso_DA = False
    ingresso_convidado = False


    escolha_ingresso = False
    while not escolha_ingresso:
        
        print("\n\tTipos de ingressos:")
        print("\t1. Inteira\n\t2. Meia-entrada\n\t3. Eng de Computação\n\t4. DA e convidados")
        tipo_ingresso = input("\n\tEscolha(número): ")
        
        if tipo_ingresso == "1":
            print("\n\tSelecionado: Inteira")
            ingresso_inteira = True

            escolha_ingresso = True

        elif tipo_ingresso == "2":
            
            print("\n\tSelecionado: Meia-entrada")
            ingresso_meia = True
            escolha_ingresso = True

            print("\n\tTipos de meia-entrada disponíveis:\n\t1.Idoso\n\t2.Estudante")
            
            tipo_meia = input("\n\tSelecione: ")
            if tipo_meia == "1":
                print("\n\tSelecionado: Idoso")
                ingresso_meia_idoso = True

            elif tipo_meia == "2":
                print("\n\tSelecionado: Estudante")
                ingreso_meia_estudante = True

            else:
                print("\n\tOpção inválida. ")
                escolha_ingresso = False


        elif tipo_ingresso == "3":
            print("\n\tSelecionado: Engenharia de Computação")
            ingresso_ecomp = True

            escolha_ingresso = True

        elif tipo_ingresso == "4":
            print("\n\tSelecionado: DA e convidados")
            print("\n\tEscolhas disponíveis:\n\t1. DA\n\t2. Convidados")
            tipo_cortesia = input("\n\tSelecione: ")
            escolha_ingresso = True

            if tipo_cortesia == "1":
                print("\n\tSelecionado: DA")
                ingresso_DA = True
                
            elif tipo_cortesia == "2":
                print("Selecionado: Convidado")
                ingresso_convidado = True
                
            else:
                escolha_ingresso = False
            
            
        else:
            print("\n\tEscolha inválida, selecione novamente.")    


#executa cada lógica de venda de forma separada
    tipo_ingresso_venda = ""
    confirma_compra = True
    if ingresso_inteira:

        print(f"\n\tO valor da compra será {valor_inteira} reais." )
        ingressos_inteira_vendidos += 1
        valor_arrecadado_inteira += valor_inteira

        tipo_ingresso_venda = "Inteira"

    elif ingresso_meia and ingresso_meia_idoso:
        
        input("Confirma que é idoso? ") #considerando o usuário como perfeito
     
        print(f"\n\tO valor da compra será {valor_meia} reais.")
        valor_arrecadado_meia += valor_meia
        ingressos_idosos_vendidos += 1
        

        tipo_ingresso_venda = "Meia-entrada-idoso"

      

    elif ingresso_meia and ingreso_meia_estudante:


        input("\n\tDigite a matrícula: ") 

        print(f"\n\tO valor da compra será {valor_meia} reais.")
        ingressos_estudante_vendidos += 1
        valor_arrecadado_meia += valor_meia

        tipo_ingresso_venda = "Meia-entrada-estudante"

    elif ingresso_ecomp:

        print(f"\n\tO valor da compra será {valor_ecomp} reais")

        valor_arrecadado_ecomp += valor_ecomp
        ingressos_ecomp_vendidos += 1

        tipo_ingresso_venda = "Estudante-ECOMP"

    elif ingresso_DA:
        
        print(f"\n\tVocê não pagará nada.")
        valor_arrecadado_DA_convidados += valor_DA
        ingressos_DA_vendidos += 1

        tipo_ingresso_venda = "DA"

    elif ingresso_convidado:
        
        print(f"\n\tVocê não pagará nada.")
        valor_arrecadado_DA_convidados += valor_DA
        ingressos_convidados_vendidos += 1

        tipo_ingresso_venda = "Convidado"

    else:
        print("\n\tTipo de ingresso inválido")

        
                
    print()
    print("#"*50)
    print("\tVenda realizada")
    print(f"\tTipo ingresso: {tipo_ingresso_venda}")
    print(f"\tCódigo: ECOMP-FEST{ingressos_disponiveis}\n")
    print("#"*50)
    ingressos_disponiveis -= 1
    
    
    if ingressos_disponiveis > 0:
        # vai alterar as comissões somente quando houver uma nova
        comissoes1 = ingressos_vendedor1//numero_vendas_para_comissao
        comissoes2 = ingressos_vendedor2//numero_vendas_para_comissao
        
        if comissoes1 > comissoes_vendedor1:
            ingressos_disponiveis -= 1
            comissoes_vendedor1 = comissoes1
            
        if comissoes2 > comissoes_vendedor2:
            ingressos_disponiveis -= 1
            comissoes_vendedor2 = comissoes2
    


    cortesias_atuais = comissoes_vendedor1+comissoes_vendedor2
    # cortesias para os vendedores não contam como ingressos vendidos
    print(f"\n\tIngressos vendidos: {numero_ingressos- (ingressos_disponiveis+cortesias_atuais)}")
    print(f"\tAinda restam {ingressos_disponiveis} ingressos disponíveis.")        


    if ingressos_disponiveis > 0:
        print("\n\tDeseja finalizar o programa?\n\t1. Sim\n\t2. Não")
        finalizar_programa = input("\tSelecione(Digíto): ")
        
        if finalizar_programa == "1":
            parar_sistema = True
            
    else:
        print("\n\tIngressos esgotados. Vendas finalizadas")
        input("\n\tPressione enter.") #necessário para interromper o fluxo e mostra o aviso


print()
print("#"*50)
print("\n\n\tEstatísticas das vendas:")

# Estatísticas de dados
total_cortesia = comissoes_vendedor1 + comissoes_vendedor2

numero_ingressos_emitidos = (ingressos_inteira_vendidos + ingressos_estudante_vendidos + total_cortesia
+ ingressos_idosos_vendidos + ingressos_ecomp_vendidos + ingressos_DA_vendidos + ingressos_convidados_vendidos)

numero_ingressos_nao_emitidos = numero_ingressos - numero_ingressos_emitidos

numero_ingressos_vendidos = numero_ingressos_emitidos - total_cortesia 

numero_ingressos_meia_vendidos = ingressos_estudante_vendidos + ingressos_idosos_vendidos


# área para exibir tudo sobre os ingressos
print("\n\tNúmero de ingressos totais emitidos:", numero_ingressos_emitidos)
print("\tNúmero de ingressos não emitidos:", numero_ingressos_nao_emitidos)

print("\n\tTotal ingressos vendidos:", numero_ingressos_vendidos)
print()
print("\tIngressos Inteira vendidos:", ingressos_inteira_vendidos)
print("\tIngressos Meia-estudante vendidos:", ingressos_estudante_vendidos)
print("\tIngressos Meia-idosos vendidos:", ingressos_idosos_vendidos)
print("\tIngressos Meia totais vendidos:", numero_ingressos_meia_vendidos)
print("\tIngressos ECOMP vendidos:", ingressos_ecomp_vendidos)
print("\tIngressos DA-doados:", ingressos_DA_vendidos)
print("\tIngressos Convidados-doados:", ingressos_convidados_vendidos)

# área para exibir cortesias
print("\n\tQuantidade total de cortesias para vendedores comissionados:", total_cortesia)
print(f"\tEra necessário vender {numero_vendas_para_comissao} ingressos para ganhar uma cortesia.")
print()
print(f"\tIngressos vendidos por {vendedor_padrao}:", ingressos_vendedor_padrao)
print(f"\tIngressos vendidos por {vendedor_convidado1}:", ingressos_vendedor1)
print(f"\tIngressos vendidos por {vendedor_convidado2}:", ingressos_vendedor2)

# apresentando valores formatados para o usúario.
valor_arrecadado = str(valor_arrecadado_inteira + valor_arrecadado_meia + valor_arrecadado_ecomp + valor_arrecadado_DA_convidados)

print(f"\n\tTotal de dinheiro arrecadado { valor_arrecadado.replace('.', ',') } reais")
print()
print(f"\tValor Inteira arrecadado: {str(valor_arrecadado_inteira).replace('.', ',')} reais")
print(f"\tValor Meia arrecadado: {str(valor_arrecadado_meia).replace('.', ',')} reais")
print(f"\tValor Ecomp arrecadado: {str(valor_arrecadado_ecomp).replace('.', ',')} reais")
print(f"\tValor DA e convidados arrecadado: {valor_arrecadado_DA_convidados} reais")


# calculando o ingresso mais vendido 
ingresso_mais_vendido_valor = max(ingressos_inteira_vendidos, ingressos_idosos_vendidos, ingressos_idosos_vendidos, ingressos_ecomp_vendidos)

ingressos_mais_vendido_nome = ''
if ingresso_mais_vendido_valor == ingressos_inteira_vendidos: ingressos_mais_vendido_nome += ", Inteira"
if ingresso_mais_vendido_valor == ingressos_estudante_vendidos: ingressos_mais_vendido_nome += ", Meia-Estudante"
if ingresso_mais_vendido_valor == ingressos_idosos_vendidos: ingressos_mais_vendido_nome += ", Meia-Idosos"
if ingresso_mais_vendido_valor == ingressos_ecomp_vendidos: ingressos_mais_vendido_nome += ", ECOMP"

# formartando saída de dados (ingresso mais vendido)
ingressos_mais_vendido_nome = ingressos_mais_vendido_nome[2::] #excluíndo a vírgula do primeiro nome
print("\n\tO(s) Ingresso(s) mais vendido(s) foi(foram):", ingressos_mais_vendido_nome)


media_idades = soma_idades/numero_ingressos_vendidos
print("\n\tA média de idades é: %.2f" % media_idades)

print()
print("#"*50)