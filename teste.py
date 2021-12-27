import json
import pandas as pd


def show_data(new_df , name='global_name', columns=['salario','nome']):
    for row in range(0,len(new_df)):
        print(name,end=" | ")
        for column in columns:
            if column == columns[-1]:
                print(new_df[column].iloc[row])
            else:
                print(new_df[column].iloc[row], end=" | ")

    
def list_salario(list_df, ascending=True, column='salario'):
    list_df=list_df.sort_values([column])
    if ascending == False:
        list_df=list_df.sort_values([column], ascending=False)
    new_df=list_df.iloc[[0]]
    for row in range(1,len(list_df)):
        if new_df[column].iloc[0] == list_df[column].iloc[row]:
            new_df=pd.concat([new_df,list_df.iloc[[row]]])
                
        else:
            break
    
    return new_df
          
        
def maior_salario(df):
    new_df=pd.DataFrame()
    df=df.sort_values(['sobrenome'])
    
    for row in range(0,len(df)):
        try:
            control=df['sobrenome'].iloc[row+1]
            
        except:
            if df['sobrenome'].iloc[row]==df['sobrenome'].iloc[row-1]:
                new_df=pd.concat([new_df,df.iloc[[row]]])
            
            break
        else:
            if control == df['sobrenome'].iloc[row]:    
                new_df=pd.concat([new_df,df.iloc[[row]]])

            else:
                if df['sobrenome'].iloc[row] == df['sobrenome'].iloc[row-1]:   
                    new_df=pd.concat([new_df,df.iloc[[row]]])
    try:
        return new_df
    except:
        return False

def get_area(df,column):
    list_column=[]
    for row in range(0,len(df)):
        data=json.loads(df.iloc[row].to_json())
        if data[column] not in list_column:
            list_column.append(data[column])
    return list_column

        

    


#1- ABRINDO O ARQUIVO JSON  
with open('funcionario.json', 'r') as json_file:
    dados = json.loads(json_file.read())

    #2- LENDO A TABELA FUNCIONARIOS
    df_full=pd.DataFrame.from_dict(dados['funcionarios'], orient='columns')
    df_areas=pd.DataFrame.from_dict(dados['areas'], orient='columns')
    #3- CRIANDO UM CAMPO E UNINDO OS CAMPOS NOME + SOBRENOME
    df_full=df_full.assign(nome_completo=lambda row: row.nome + ' ' + row.sobrenome)

    
    #INICIO ATIVIDADE 1
    show_data(list_salario(df_full)                   , name='global_min', columns=['nome_completo','salario'])
    show_data(list_salario(df_full, ascending=False), name='global_max', columns=['nome_completo','salario'])
    show_data(pd.DataFrame.from_dict([{'salario':df_full.salario.mean()}],orient='columns'), name='global_avg', columns=['salario'])
    
    
    df_min=list_salario(df_full)
    df_max=list_salario(df_full, ascending=False)
    media_salario = df_full.salario.mean()
    #FIM DA ATIVIDADE 1
    
    #INICIO DA ATIVIDADE 2
    lista_area=get_area(df_full,'area')
    df_temp=df_full.groupby(df_full.area)
    df_avg=pd.DataFrame()
    
    for i in range(0,len(lista_area)):
        nome=lista_area[i]
        show_data(list_salario(df_temp.get_group(nome).assign(area_completa=df_areas['nome'].iloc[i]), ascending=False), name='area_max', columns=['area_completa','nome_completo','salario'])
        show_data(list_salario(df_temp.get_group(nome).assign(area_completa=df_areas['nome'].iloc[i])), name='area_min', columns=['area_completa','nome_completo','salario'])
    for i in range(0,len(lista_area)):
        nome=lista_area[i]
        dict_avg=[{
        'area_completa':df_areas['nome'].iloc[i],
        'salario':round(df_temp.get_group(nome)['salario'].mean(),2)
        }]
        df_temp_avg=pd.DataFrame.from_dict(dict_avg,orient='columns')
        show_data(df_temp_avg, name='area_avg', columns=['area_completa','salario'])
    
        df_avg=pd.concat([df_avg,df_temp_avg])

    




    
    
    df_sd=df_temp.get_group('SD').assign(area_completa=df_areas['nome'].iloc[0])
    df_sd_min=list_salario(df_sd)
    df_sd_max=list_salario(df_sd, ascending=False)
    
    df_sm=df_temp.get_group('SM').assign(area_completa=df_areas['nome'].iloc[1])
    df_sm_min=list_salario(df_sm)
    df_sm_max=list_salario(df_sm, ascending=False)
    
    df_ud=df_temp.get_group('UD').assign(area_completa=df_areas['nome'].iloc[2])
    df_ud_min=list_salario(df_ud)
    df_ud_max=list_salario(df_ud, ascending=False)
    
    df_sd=df_temp.get_group('SD')['salario'].mean()
    df_sm=df_temp.get_group('SM')['salario'].mean()
    df_ud=df_temp.get_group('UD')['salario'].mean()
  
    list_areas=[row for row in df_areas['codigo']]
    
    #FIM DA ATIVIDADE 2
    
    #INICIO DA ATIVIDADE 3
    len_area=[ len(df_full.groupby(df_full.area).get_group(list_areas[length])) for length in range(0,len(list_areas))]
    df_funcionario=df_areas.assign(qtd_funcionario=len_area)    
    show_data(list_salario(df_funcionario, ascending=False, column='qtd_funcionario') , name='most_employees', columns=['nome','qtd_funcionario'])
    show_data(list_salario(df_funcionario, column='qtd_funcionario') , name='least_employees', columns=['nome','qtd_funcionario'])
    
    #FIM DA ATIVIDADE # 
    
    #ATIVIDADE 4
    df_lastname=maior_salario(df_full)
    lista_lastname=get_area(df_lastname,'sobrenome')
    df_temp_lastname=df_lastname.groupby(df_lastname.sobrenome)
    for name in lista_lastname:
        
        show_data(list_salario(df_temp_lastname.get_group(name), ascending=False) , name='last_name_max', columns=['sobrenome','nome_completo','salario'])
    
    #FIM DA ATIVIDADE
<<<<<<< HEAD
   
=======
   
>>>>>>> 2378732fe17aa2c6bf59aac49820e7f126fa4c44
