telefone = input("digite o telefone no formato (xx)xxxxx-xxxx: ")







data = input("Digite a data no formato dd/mm/aaaa: ")

dia = data{0:2}
mes = data{3:5}
ano = data{6:}

print("Dia:", {dia})
print("Mês:", {mes})
print("Ano:", {ano})

email = input("Digite o e-mail: (nome.sobrenome@escola.com) ")

primeiro_nome = email.[0:5]
dominio = email.[13:]

print(f"Primeiro nome extraido: {primeiro_nome}")
print(f"Domínio extraido: {dominio}")