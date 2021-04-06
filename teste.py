import json
import pandas as pd

class dataProcessing:
    pass



#1- ABRINDO O ARQUIVO JSON  
with open('funcionario.json', 'r') as json_file:
    dados = json.loads(json_file.read())

    #2- LENDO A TABELA FUNCIONARIOS
    df_full=pd.DataFrame.from_dict(dados['funcionarios'], orient='columns')
    #3- CRIANDO UM CAMPO E UNINDO OS CAMPOS NOME + SOBRENOME
    df_full['nome_completo']=\
    df_full.apply(lambda row: row.nome + ' ' + row.sobrenome, axis=1)

    #INICIANDO A FUNÇÃO
    group=df_full[['nome_completo','salario']]
    salario=df_full.salario
    temp=0
    df_max={}
    df_min={}

    #4- FUNÇÃO PARA CONFERIR E SALVAR O MAIOR SALARIO E O NOME AND SALVAR SALARIOS IGUAIS
    for i in range(len(df_full)):
        if temp<=salario[i]: #CONFERE SE SALARIO É MAIOR OU IGUAL A TEMP
            if temp != salario[i]: #VERIFICA SE TEMP É DIFERENTE AO SALARIO
                temp=salario[i]
                df_max.clear() #LIMPA O DF_MAX SE ELE FOR DIFERENTE E ENTRA NO PROXIMO IF E SALVA O SALARIO

            if temp == salario[i]:
                temp=salario[i]
                df_list=list(group.iloc[i])
                df_max[df_list[0]]=df_list[1] #GERA UMA DICT COM NOME:SALARIO
                #No final da execução do for terá um temp com o valor máximo
    
    for rows in range(len(df_full)): #SEGUE A MESMA LÓGICA QUE PARA O SALARIO MÁXIMO
        if temp>=salario[rows]:
            if temp != salario[rows]:
                temp=salario[rows]
                df_min.clear()

            if temp == salario[rows]:
                temp=salario[rows]
                df_list=list(group.iloc[rows])
                df_min[df_list[0]]=df_list[1]