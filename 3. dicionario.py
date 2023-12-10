# Crie um dicionário
pessoa = {
    "nome": "Paulo",
    "idade": 50,
    "endereco": "Sidney Chaves",
    "nacionalidade": "Brasileiro"
}

# mostre o nome em tela
print(pessoa["nome"])

# mostre a idade em tela
print(pessoa["idade"])

# mostre as informações em tela
print(
    pessoa["nome"] + 
    " possui " + 
    str(pessoa["idade"]) + 
    " anos de idade. Ele é " + 
    pessoa["nacionalidade"]
)