import math

# Biblioteca de Capitais do Brasil
capitais_brasil = {
    "Brasília": {"populacao": 2817068},
    "São Paulo": {"populacao": 11451245},
    "Rio de Janeiro": {"populacao": 6211423},
    "Belo Horizonte": {"populacao": 2315560},
    "Salvador": {"populacao": 2418005},
    "Curitiba": {"populacao": 1773733},
    "Fortaleza": {"populacao": 2428678},
    "Recife": {"populacao": 1488920},
    "Porto Alegre": {"populacao": 1332570},
    "Manaus": {"populacao": 2063547},
    "Belém": {"populacao": 1303389},
    "Goiânia": {"populacao": 1437237},
    "Cuiabá": {"populacao": 650912},
    "Natal": {"populacao": 751300},
    "Vitória": {"populacao": 322869},
    "São Luís": {"populacao": 1037775},
    "Teresina": {"populacao": 866300},
    "João Pessoa": {"populacao": 833932},
    "Campo Grande": {"populacao": 897938},
    "Maceió": {"populacao": 957916},
    "Florianópolis": {"populacao": 537213},
    "Aracaju": {"populacao": 602757},
    "Porto Velho": {"populacao": 460413},
    "Boa Vista": {"populacao": 413486},
    "Palmas": {"populacao": 302692},
    "Rio Branco": {"populacao": 364756},
    "Macapá": {"populacao": 442933}  # Fix the missing populacao here
}

def calcular_tamanho_amostra(tamanho_populacao, margem_erro):
    z = 1.96  # Valor Z para um nível de confiança de 95%
    
    p = 0.5  # Proporção assumida (0.5 para variabilidade máxima)
    e = margem_erro
    
    tamanho_amostra = (z**2 * p * (1 - p)) / (e**2) / (1 + ((z**2 * p * (1 - p)) / (e**2 * tamanho_populacao)))
    return math.ceil(tamanho_amostra)

# Entrada dos dados
nome_populacao = input("Digite o nome da cidade: ")

if nome_populacao in capitais_brasil:
    tamanho_populacao = capitais_brasil[nome_populacao]["populacao"]
    print(f"População de {nome_populacao}: {tamanho_populacao}")
    margem_erro = float(input("Digite a margem de erro desejada: "))
else:
    tamanho_populacao = int(input("Digite o tamanho da população: "))
    margem_erro = float(input("Digite a margem de erro desejada: "))

tamanho_amostra = calcular_tamanho_amostra(tamanho_populacao, margem_erro)
print(f"Para a população '{nome_populacao}', o tamanho de amostra necessário é: {tamanho_amostra}")
