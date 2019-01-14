#
#  Exemplo de Filtragem Baseada em Conteudo
#
#  Atributos:
#  Tipo: 1 = esportivo; 2 = classico; 3 = familiar; 4 = utilitario; 5 = popular
#  Combustivel: 1 = gasolina; 2 = alcool; 3 = flex; 4 = gas; 5 = diesel
#  Cor: 1 = branco; 2 = vermelho; 3 = prata; 4 = vinho; 5 = preto
#  Valor: 1 = <20.000; 2 = >20.000 & < 30.000; 3 = >30.000 & <60.000; 4 = > 60.000 & <100.000; 5 => >100.000
#  Fabricacao: 1 = novo; 2 = seminovo; 3 = usado
#  Local: 1 = nacional; 2 = importado
#  Manutencao: 1=baixa; 2=media; 3=alta; 4=muito alta
# Segurança: 1=baixa; 2=media; 3=alta
# Conforto: 1=baixo; 2=medio; 3=alto

#  Para testar digite recommend('Bonifacio', carros)
#


from math import sqrt

#  Dataset de carros

carros = {"Carro1": {"tipo": 4, "combustivel": 1, "cor": 2, "valor": 2, "fabricacao": 1, "local": 1, "Manutencao":2},
         "Carro2": {"tipo": 1, "combustivel": 2, "cor": 5, "valor": 5, "fabricacao": 1, "local": 2},
         "Carro3": {"tipo": 3, "combustivel": 3, "cor": 3, "valor": 3, "fabricacao": 2, "local": 1},
         "Carro4": {"tipo": 4, "combustivel": 5, "cor": 1, "valor": 4, "fabricacao": 2, "local": 1},
         "Carro5": {"tipo": 2, "combustivel": 2, "cor": 4, "valor": 2, "fabricacao": 1, "local": 1},
         "Carro6": {"tipo": 5, "combustivel": 1, "cor": 2, "valor": 1, "fabricacao": 3, "local": 1},
         "Carro7": {"tipo": 1, "combustivel": 1, "cor": 2, "valor": 5, "fabricacao": 1, "local": 2},
         "Carro8": {"tipo": 5, "combustivel": 3, "cor": 3, "valor": 2, "fabricacao": 1, "local": 1},
         "Carro9": {"tipo": 4, "combustivel": 5, "cor": 5, "valor": 4, "fabricacao": 2, "local": 1},
         "Carro10": {"tipo": 2, "combustivel": 2, "cor": 2, "valor": 3, "fabricacao": 1, "local": 2},}

#  Perfil do usuario
perfilDoUsuario = {"Bonifacio": {"tipo": 1, "combustivel": 2, "cor": 5, "valor": 5, "fabricacao": 1, "local": 2}}



#  Calcula a similaridade entre o perfil do usuario com o perfil de cada carro do dataset
def manhattan(carros, perfilDoUsuario):
    """Computes the Manhattan distance. """
    distance = 0
    total = 0
    for key in carros:
        if key in perfilDoUsuario:
            distance += abs(carros[key] - perfilDoUsuario[key])
            total += 1
    return distance


# Excuta a recomenda de carros para um determinado usuario
def recommend(userName, carros):
    """creates a sorted list of cars based on their distance to perfilDoUsuario"""
    distances = []
    for carro in carros:
        distance = manhattan(carros[carro], perfilDoUsuario[userName])
        distances.append((distance, carro))
    # sort based on distance -- closest first
    distances.sort()
    return distances

print(recommend("Bonifacio", carros))


