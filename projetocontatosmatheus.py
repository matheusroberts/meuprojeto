# PROJETO GERENCIADOR DE CONTATOS 
# MODULO 1 PYTHON - ROCKETSEAT
def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {
        "Nome": nome_contato,
        "Telefone": telefone_contato,
        "Email": email_contato,
        "Favoritado": False
    }
    contatos.append(contato)
    print(f"O contato {nome_contato} foi adicionado a sua lista de contatos com sucesso!")

def ver_contatos(contatos):
    print("\nLista de contatos: ")
    for indice, contato in enumerate(contatos, start=1):
        status_favorito = "♡" if contato["Favoritado"] else " "
        print(f"{indice}. Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']} {status_favorito}")

def atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado] = {
            "Nome": novo_nome,
            "Telefone": novo_telefone,
            "Email": novo_email,
            "Favoritado": contatos[indice_contato_ajustado].get("Favoritado", False)
        }
        print(f"Contato {indice_contato} atualizado com sucesso!")
    else:
        print(f"Índice {indice_contato} inválido. Não há contato com esse número.")

def favoritar_contatos(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["Favoritado"] = True
        print(f"Contato {indice_contato} marcado como favorito!")
    else:
        print(f"Índice {indice_contato} inválido. Não há contato com esse número.")

def desfavoritar_contatos(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["Favoritado"] = False
        print(f"Contato {indice_contato} desmarcado como favorito!")
    else:
        print(f"Índice {indice_contato} inválido. Não há contato com esse número.")

def listar_favoritos(contatos):
    print("\nLista de contatos favoritos: ")
    favoritos = [contato for contato in contatos if contato["Favoritado"]]
    if favoritos:
        for indice, contato in enumerate(favoritos, start=1):
            print(f"{indice}. Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']} ♡")
    else:
        print("Nenhum contato foi favoritado ainda.")

def apagar_contato(contatos, indice_contatos):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contato_removido = contatos.pop(indice_contato_ajustado)
        print(f"O contato {contato_removido ['Nome']}" 'foi removido com sucesso')

    else:
        print(f"O contato {indice_contato} é invalido. Não há contato com esse número.")

contatos = []
while True:
    print("\nMenu gerenciador de contatos")
    print("1. Adicionar contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar contatos")
    print("4. Marcar contato como favorito")
    print("5. Desmarcar contato como favorito")
    print("6. Lista de contatos favoritos")
    print("7. Apagar um contato")
    print("8. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do seu contato: ")
        print(f"O contato com o nome {nome_contato} foi cadastrado!")
        telefone_contato = input("Digite o numero de telefone do seu contato: ")
        print(f"O contato com o telefone {telefone_contato} foi cadastrado!")
        email_contato = input("Digite o e-mail do seu contato: ")
        print(f"O contato com o e-mail {email_contato} foi cadastrado!")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
        
    elif escolha == "2":
        ver_contatos(contatos)
        
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input("Digite o novo e-mail do contato: ")
        atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja favoritar: ")
        favoritar_contatos(contatos, indice_contato)

    elif escolha == "5":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja desmarcar como favorito: ")
        desfavoritar_contatos(contatos, indice_contato)

    elif escolha == "6":
        listar_favoritos(contatos)

    elif escolha == "7":
        ver_contatos(contatos)
        indice_contato = input ("Digite o numero do contato que deseja deletar: ")
        apagar_contato(contatos, indice_contato)

    elif escolha == "8":
        break

print("Programa finalizado")