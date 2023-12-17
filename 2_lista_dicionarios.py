import pandas as pd

list_users = [
    {
        "nome": "Paulo",
        "idade": 22,
        "sexo": "masculino",
        "nacionalidade": "brasileira",
        "salario": 5600
    },
    {
        "nome": "Claudio",
        "idade": 18,
        "sexo": "masculino",
        "nacionalidade": "brasileira",
        "salario": 3500
    },
    {
        "nome": "Maria",
        "idade": 25,
        "sexo": "feminino",
        "nacionalidade": "brasileira",
        "salario": 4200
    },
    {
        "nome": "João",
        "idade": 30,
        "sexo": "masculino",
        "nacionalidade": "brasileira",
        "salario": 9500

    },
    {
        "nome": "Ana",
        "idade": 20,
        "sexo": "feminino",
        "nacionalidade": "brasileira",
        "salario": 0

    },
    {
        "nome": "Pedro",
        "idade": 18,
        "sexo": "masculino",
        "nacionalidade": "brasileira",
        "salario": 4578

    },
    {
        "nome": "José",
        "idade": 22,
        "sexo": "masculino",
        "nacionalidade": "brasileira",
        "salario": 1500
    },
    {
        "nome": "Julia",
        "idade": 20,
        "sexo": "feminino",
        "nacionalidade": "brasileira",
        "salario": 1500

    },
    {
        "nome": "Lucas",
        "idade": 18,
        "sexo": "masculino",
        "nacionalidade": "brasileira",
        "salario": 1500
    },
    {
        "nome": "Mariana",
        "idade": 25,
        "sexo": "feminino",
        "nacionalidade": "brasileira",
        "salario": 1500
    }
]

# 1. Mostre no terminal a lista de usuários
print('LISTA',list_users)

# 2. Criar um DataFrame da lista de usuários
df_usuarios = pd.DataFrame(list_users)
print('DATA_FRAME',df_usuarios)

# 3. Descreva o dataframe
print(df_usuarios.describe())

# 4. Descreva as colunas do dataframe
print(df_usuarios.columns)

# 5. Obter a média de idade
print(df_usuarios.mean(numeric_only=True))

# 6. Obter o tamanho do DataFrame
print('TAMANHO',df_usuarios.size)

# 7. Obter a quantidade de linhas
print('QTD_LINHAS',len(df_usuarios))

# 7. Obter a média de idade
print(df_usuarios["idade"].mean())

# 7. Obter a soma dos salários
print(df_usuarios["salario"].describe())

# 8. Obter a média de salário pelo sexo
print("**********************************")
print(df_usuarios.groupby('sexo')['salario'].mean())

# 9. Obter a média de idade pelo sexo
print("**********************************")
print(df_usuarios.groupby('sexo')['idade'].mean())

df_test = df_usuarios.groupby('sexo')['idade'].mean()
# print(type(df_test))
df_test.to_json('teste.json')



