from pandas import Series, DataFrame
import pandas as pd
from collections import OrderedDict
import csv
import recommender as rec
import avaliar as ava
#//////////////////////////////////////Dataset Casos////////////////////////////////////

casos_leitura = pd.read_csv("C:/Users/User Acer/Desktop/Paic/Datasets/CBR/Casos_CaseBasedReasoning.csv")
casos = pd.DataFrame(casos_leitura,columns=['Conforto','Seguranca','GastosFixos','Desempenho','Carroceria','NumLugares','NumeroDePortas','Finalidade','Combustivel','Valor','RecomendacoesRelevantes'])

#///////////////////////////////////////Dataset Automoveis//////////////////////////////
dataset = pd.read_csv("C:/Users/User Acer/Desktop/Paic/Datasets/DatasetCarrosFiltConteudo.csv")
df = pd.DataFrame(dataset, columns=['Marca','Modelo','Ano','Concessionaria','Conforto','Seguranca','GastosFixos','Desempenho','Carroceria','NumLugares','NumeroDePortas','Finalidade','Combustivel','Valor','SensorDeEstacionamento','ArCondicionado','Bluetooth','Direcao','BancoCouro','GPS','VidrosEletricos','PilotoAutomatico','TetoSolar','TamPortaMala','Cacamba','ComputadorBordo','DisponibiliPeca','Airbag','ABS','Blindagem','FarolNeblina','IPVA','ConsumoGasolina','Seguro','Manutencao','Motor','CavalosForca','VelMaxima'])

df['Conforto'] = df[['SensorDeEstacionamento','ArCondicionado','Bluetooth','Direcao','BancoCouro','GPS','VidrosEletricos','PilotoAutomatico','TetoSolar','TamPortaMala','Cacamba','ComputadorBordo']].mean(axis=1)
df['Seguranca'] = df[['DisponibiliPeca','Airbag','ABS','Blindagem','FarolNeblina']].mean(axis=1)
df['GastosFixos'] = df[['IPVA','ConsumoGasolina','Seguro','Manutencao']].mean(axis=1)
df['Desempenho'] = df[['IPVA','ConsumoGasolina','Seguro','Manutencao']].mean(axis=1)

df.drop(['SensorDeEstacionamento','ArCondicionado','Bluetooth','Direcao','BancoCouro','GPS','VidrosEletricos','PilotoAutomatico','TetoSolar','TamPortaMala','Cacamba','ComputadorBordo','DisponibiliPeca','Airbag','ABS','Blindagem','FarolNeblina','IPVA','ConsumoGasolina','Seguro','Manutencao','Motor','CavalosForca','VelMaxima'], axis=1, inplace=True)

training_dataset = pd.DataFrame(dataset, columns=['Marca','Modelo','Ano','Concessionaria','Conforto','Seguranca','GastosFixos','Desempenho','Carroceria','NumLugares','NumeroDePortas','Finalidade','Combustivel','Valor','SensorDeEstacionamento','ArCondicionado','Bluetooth','Direcao','BancoCouro','GPS','VidrosEletricos','PilotoAutomatico','TetoSolar','TamPortaMala','Cacamba','ComputadorBordo','DisponibiliPeca','Airbag','ABS','Blindagem','FarolNeblina','IPVA','ConsumoGasolina','Seguro','Manutencao','Motor','CavalosForca','VelMaxima'])
training_dataset.drop(['Concessionaria','Conforto','Seguranca','GastosFixos','Desempenho','Carroceria','NumLugares','NumeroDePortas','Finalidade','Combustivel','Valor','SensorDeEstacionamento','ArCondicionado','Bluetooth','Direcao','BancoCouro','GPS','VidrosEletricos','PilotoAutomatico','TetoSolar','TamPortaMala','Cacamba','ComputadorBordo','DisponibiliPeca','Airbag','ABS','Blindagem','FarolNeblina','IPVA','ConsumoGasolina','Seguro','Manutencao','Motor','CavalosForca','VelMaxima'], axis=1, inplace=True)

#//////////////////////////////Media ponderada////////////////////////////////////////////

def metriSimiGlobal(Pesos, Notas):

    notasIndividuais = []
    if len(Pesos) != len(Notas):
        print("Tamanho lista pesos e Tamanho lista notas diferente")
        return 0

    else:
        for i in range(len(Notas)):
            notasIndividuais.append(Pesos[i]*Notas[i])

    soma = sum(notasIndividuais)
    similaridade = soma/len(notasIndividuais)
    return similaridade

#//////////////////////////////////Calculo da similaridade//////////////////////////////////
def calcSimi(novo, Caso):
    pesos = [1,1,1,1,1,1,1,1,1,1]
    similaridadeLocal = rec.cos_sim(novo, Caso)
    similaridadeCBR = metriSimiCaseBased(pesos, similaridadeLocal)
    return similaridadeCBR

#///////////////////////////////////Aprender casos//////////////////////////////////////////
def LearnCaseBased(Case):
    with open('C:/Users/User Acer/Desktop/Paic/Datasets/CBR/Casos_CaseBasedReasoning.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(Case)

#/////////////////////////////////////Recomendar atraves dos casos//////////////////////////
def recByCases(UserCase):
    distances=[]
    tam=casos.shape[0]
    compare = list(UserCase.values())
    for i in range(tam):
        caso = casos.iloc[i]
        similarity = calcSimi(list(UserCase), list(caso)[:1])
        distances.append((similarity, list(carro)[1:]))
    distances.sort()
    distances.reverse() # ---- Pearson and Cosseno

    print(distances[:3])
    return distances


#/////////////////////////////////////Aprendizado Inicial///////////////////////////////////



#///////////////////////////////////////MAIN////////////////////////////////////////////////

Usuario = {"Carroceria": 1.5,"NumLugares": 5,"NumeroDePortas": 3,"Finalidade": 1,"Combustivel": 2,"Valor": 4,"Conforto": 2,"Seguranca": 2,"GastosFixos": 1,"Desempenho": 1}

rec.recommend(Usuario,df)