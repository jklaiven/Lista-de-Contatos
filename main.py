contato = {}

contato['nome'] = input("Digite o nome do contato: ")
contato['telefone'] = input("Digite o número de telefone: ")
contato['email'] = input("Digite o endereço de email: ")

print("\nInformações do contato:")
for chave, valor in contato.items():
    print(f"{chave}: {valor}")
