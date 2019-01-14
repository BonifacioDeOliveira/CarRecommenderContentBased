#


#  Para testar digite recommend('Bonifacio', dataset)
import random
from math import sqrt
from collections import OrderedDict
import time
import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import csv
#from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import mode
import recommender as rec
import avaliar as ava
from sklearn.metrics import average_precision_score
#importando dataset e nomeando como dataset


#///////////////////////////////////////////// DATASET - CARREGANDO E TRATANDO //////////////////////////////////////////////////////////////////////////////

dataset = pd.read_csv("C:/Users/User Acer/Desktop/Paic/Datasets/DatasetCarrosFiltConteudo.csv")
df = pd.DataFrame(dataset, columns=['Marca','Modelo','Ano','Concessionaria','Conforto','Seguranca','GastosFixos','Desempenho','Carroceria','NumLugares','NumeroDePortas','Finalidade','Combustivel','Valor','SensorDeEstacionamento','ArCondicionado','Bluetooth','Direcao','BancoCouro','GPS','VidrosEletricos','PilotoAutomatico','TetoSolar','TamPortaMala','Cacamba','ComputadorBordo','DisponibiliPeca','Airbag','ABS','Blindagem','FarolNeblina','IPVA','ConsumoGasolina','Seguro','Manutencao','Motor','CavalosForca','VelMaxima'])

df['Conforto'] = df[['SensorDeEstacionamento','ArCondicionado','Bluetooth','Direcao','BancoCouro','GPS','VidrosEletricos','PilotoAutomatico','TetoSolar','TamPortaMala','Cacamba','ComputadorBordo']].mean(axis=1)
df['Seguranca'] = df[['DisponibiliPeca','Airbag','ABS','Blindagem','FarolNeblina']].mean(axis=1)
df['GastosFixos'] = df[['IPVA','ConsumoGasolina','Seguro','Manutencao']].mean(axis=1)
df['Desempenho'] = df[['IPVA','ConsumoGasolina','Seguro','Manutencao']].mean(axis=1)

df.drop(['SensorDeEstacionamento','ArCondicionado','Bluetooth','Direcao','BancoCouro','GPS','VidrosEletricos','PilotoAutomatico','TetoSolar','TamPortaMala','Cacamba','ComputadorBordo','DisponibiliPeca','Airbag','ABS','Blindagem','FarolNeblina','IPVA','ConsumoGasolina','Seguro','Manutencao','Motor','CavalosForca','VelMaxima'], axis=1, inplace=True)

training_dataset = pd.DataFrame(dataset, columns=['Marca','Modelo','Ano','Concessionaria','Conforto','Seguranca','GastosFixos','Desempenho','Carroceria','NumLugares','NumeroDePortas','Finalidade','Combustivel','Valor','SensorDeEstacionamento','ArCondicionado','Bluetooth','Direcao','BancoCouro','GPS','VidrosEletricos','PilotoAutomatico','TetoSolar','TamPortaMala','Cacamba','ComputadorBordo','DisponibiliPeca','Airbag','ABS','Blindagem','FarolNeblina','IPVA','ConsumoGasolina','Seguro','Manutencao','Motor','CavalosForca','VelMaxima'])
training_dataset.drop(['Concessionaria','Conforto','Seguranca','GastosFixos','Desempenho','Carroceria','NumLugares','NumeroDePortas','Finalidade','Combustivel','Valor','SensorDeEstacionamento','ArCondicionado','Bluetooth','Direcao','BancoCouro','GPS','VidrosEletricos','PilotoAutomatico','TetoSolar','TamPortaMala','Cacamba','ComputadorBordo','DisponibiliPeca','Airbag','ABS','Blindagem','FarolNeblina','IPVA','ConsumoGasolina','Seguro','Manutencao','Motor','CavalosForca','VelMaxima'], axis=1, inplace=True)

#/////////////////////////////////////////////////////////// PERFIL DO USUARIO //////////////////////////////////////////////////////////////////////////////

#  Perfil do usuario
Usuario = {"Conforto": 2,"Seguranca": 2,"GastosFixos": 1,"Desempenho": 1,"Carroceria": 1.5,"NumLugares": 5,"NumeroDePortas": 3,"Finalidade": 1,"Combustivel": 2,"Valor": 4}
key = ["Conforto","Seguranca","GastosFixos","Desempenho","Carroceria","NumLugares","NumeroDePortas","Finalidade","Combustivel","Valor"]
user = []
for j in key:
    user.append(Usuario[j])

#///////////////////////////////////////////// METRICAS DE SIMILARIDADE /////////////////////////////////////////////////////////////////////////////////////

#No pacote recommender

#////////////////////////////////////////////////////////////RECOMMENDER ////////////////////////////////////////////////////////////////////////////////////
# Excuta a recomendacao de carros para um determinado usuario


#No pacote recommender

#///////////////////////////////////////////////////SEPARA O DATASET DE FORMA ALEATORIA E SALVA EM UM CSV///////////////////////////////////////////////////
#Seleciona Carros Aleatorios
'''
for x in range(75):
    rand = random.randint(0,(training_dataset.shape[0])-1)
    training_dataset.drop(training_dataset.index[rand], axis=0, inplace=True)

#Sera ececutado uma vez e salvo em um arquivo
training_dataset['selected'] = pd.Series(0, index=training_dataset.index)
training_dataset.reset_index(drop=True, inplace=True)

training_dataset.to_csv('training dataset', index=True)

print(training_dataset)
print("\n")
'''
#     FOI GERADO E SALVO UMA SO VEZ
#     NAO APAGAR EM HIPOTESE ALGUMA
#//////////////////////////////////////////////////GERA A SELECAO PARA COMPARACAO DOS AUTOMOVEIS DO DATASET DE TREINO///////////////////////////////////////

train_dataset = pd.read_csv("C:/Users/User Acer/Desktop/Paic/Datasets/training_dataset.csv")
training_dataset = pd.DataFrame(train_dataset, columns=['ID','Marca','Modelo','Ano','selected'])
training_dataset.drop(['ID', 'selected'],axis=1, inplace=True)
print(training_dataset)

selected = []
selected_numbers = 0
IDS = []
entrada = 1
print("Quais carros lhe interessam? digitar o numero e selecionar 'Enter', ao terminar digitar e selecionar '-1'")
while(entrada != -1): #Vai preencher uma lista com os carros selecionados
    entrada = int(input("ID do Carro: "))
    if entrada != -1:
        if entrada in IDS:
            print("Carro ja selecionado")
        else:
            selected.append(list(training_dataset.iloc[entrada]))
            IDS.append(entrada)

tam = df.shape[0]
user_selected = []
for car in selected: #Vai preencher uma lista com os carros selecionados junto dos respectivos atributos
   #print(car)
    for i in range(tam - 1):
        carro = df.iloc[i]
        if ((list(carro)[:11])[1] == car[1]):
            user_selected.append(list(carro))

selected_numbers = len(selected)
print(selected_numbers)

# RETORNA A LISTA "user_selected"

#////////////////////////////////////////////// METRICAS DE AVALIACAO ///////////////////////////////////////////////////////////////////////////////////////

#No pacote metricasAva

#/////////////////////////////////////////////ARMAZENA AS NOTAS PARA COMPARACAO//////////////////////////////////////////////////////////////////////////////
'''
def armazenarNotas(pre,re,Fme):
    with open('C:/Users/User Acer/Desktop/Paic/Datasets/Avaliacao/avaliacoes.csv', 'a') as f:
        writer = csv.writer(f)
        pre = float("{0:.3f}".format(pre))
        re = float("{0:.3f}".format(re))
        Fme = float("{0:.3f}".format(Fme))

        writer.writerow([pre,re,Fme])

#///////////////////////////////////////////// PROCEDIMENTOS COM A AVALIACAO ////////////////////////////////////////////////////////////////////////////////

#sera considerado 3 como numrecomendados
def avaliar(selected):
    relevantes = int(input("Sera medida a precisao, digitar a quantidade de automoveis relevantes e tecle 'Enter': "))

    if relevantes <= 3 and relevantes >=0:

        pre = ava.precisao(relevantes, 3)
        #print(pre)
        re = ava.recall(relevantes, selected)
        #print(re)
        Fme = ava.F_measure(relevantes, 3, selected)
        #print(Fme)

        armazenarNotas(pre,re,Fme)

        print("a precisao e: %1.4f" %pre)
        print("o recall e: %1.4f" %re)
        print("Fmeasure e: %1.4f" %Fme)

    else:

        print("Valor invalido, tente novamente: ")
        avaliar(selected)

#//////////////////////////////////////////////////AVALIAR SISTEMA///////////////////////////////////////////////////////////////////////////////////////////
#TRABALHA COM LEITURA DO DATASET AVALIACAO E CALCULA A MEDIA DAS AVALIACOES

def avaliasistema():
    avalia = pd.read_csv("C:/Users/User Acer/Desktop/Paic/Datasets/Avaliacao/avaliacoes.csv")
    avalia_dataset = pd.DataFrame(avalia, columns=['pre','re','Fme'])

    soma = sum(avalia_dataset["Fme"].values)
    media = soma/(len(avalia_dataset["Fme"].values))

    return(media)
'''
#//////////////////////////////////////////////////////RACIOCINIO BASEADO EM CASOS///////////////////////////////////////////////////////////////////////////

#No pacote CaseBased.py

#///////////////////////////////////////////////////////  MAIN  /////////////////////////////////////////////////////////////////////////////////////////////


rec.recommend(user, df)
#ava.avaliar(selected_numbers)
#print(ava.avaliasistema())
