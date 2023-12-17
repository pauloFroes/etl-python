lista = [10,"Paulo",50]

# Criar uma lista de números
lista_numeros = [1, 50, 25, 90]

# Mostra essa lista no terminal
print(lista)

# Crie uma lista com outras listas
lista_mult = [1, "Paulo", [1,2,3,4]]

# Crie uma lista de dicionários (pessoas)
lista_de_pessoas = [
    {
        "nome": "Paulo",
        "idade": 50,
        "endereco": "Sidney Chaves",
        "nacionalidade": "Brasileiro"
    },
    {
        "nome": "Fran",
        "idade": 25,
        "endereco": "Vila Velha",
        "nacionalidade": "Brasileira"
    }
]

# Adicione uma nova pessoa nessa lista
lista_de_pessoas.append(
    {
        "nome": "João",
        "idade": 30,
        "endereco": "Vitória",
        "nacionalidade": "Brasileira"
    }
) 

# Remover a posição 2 da lista
del lista_de_pessoas[-1]

# Mostre no terminal a lista das pessoas
print(lista_de_pessoas)