print('Bem-vindo ao menu de cadastramento')

funcionarios = []

while True:
    print('\n--- Cadastrar novo funcionário ---\n')

    print('1. Cadastrar funcionário')
    print('2. Listar funcionários')
    print('3. Sair')

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        print('Cadastrar funcionário')

        nome_funcao = input('Digite manualmente a função do funcionário: ')

        funcionario = {
            'nome': input('Digite o nome do funcionário: '),
            'cpf': input('Digite o CPF: '),
            'email': input('Digite o email: '),
            'telefone': input('Digite o telefone: '),
            'endereco': input('Digite o endereço: '),
            'funcao': nome_funcao
        }

        funcionarios.append(funcionario)
        print(f"Funcionário {funcionario['nome']} cadastrado na função {funcionario['funcao']}!")

    elif opcao == '2':
        print('\nListar funcionários')

        if not funcionarios:
            print('Nenhum funcionário cadastrado.')
        else:
            for funcionario in funcionarios:
                print(f"Nome: {funcionario['nome']}")
                print(f"CPF: {funcionario['cpf']}")
                print(f"Email: {funcionario['email']}")
                print(f"Telefone: {funcionario['telefone']}")
                print(f"Endereço: {funcionario['endereco']}")
                print(f"Função: {funcionario['funcao']}\n")

    elif opcao == '3':
        print('Finalizando programa')
        break

    else:
        print('Opção inválida.')








