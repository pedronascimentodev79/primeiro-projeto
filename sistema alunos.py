banco_de_dados = []
matricula_atual = 0

def criarAluno(nome, idade, curso):
    global matricula_atual
    matricula_atual += 1
    aluno = {
        'matricula': matricula_atual,
        'nome': nome,
        'idade': idade,
        'curso': curso
    }

    return aluno

def adicionarAluno(nome, idade, curso):
    aluno = criarAluno(nome, idade, curso)
    banco_de_dados.append(aluno)
    print('Aluno Adicionado Com Sucesso!')

def listarTodosAlunos():
    print('---- Alunos Matriculados ----')
    for aluno in banco_de_dados:
        print(f'Matricula: {aluno["matricula"]}')
        print(f'Nome: {aluno["nome"]}')
        print(f'Idade: {aluno["idade"]}')
        print(f'Curso: {aluno["curso"]}')
        print('------------------------\n')

def editarAluno(matricula, nome, idade, curso):
    aluno = alunoExiste(matricula)
    if aluno:

        aluno['nome'] = nome
        aluno['idade'] = idade
        aluno['curso'] = curso
        print('Dados Alterados Com Sucesso!')
    else:
        print('Matricula Informada não Encontrada!')

def alunoExiste(matricula):
    for aluno in banco_de_dados:
        if aluno['matricula'] == matricula:
            return aluno
    return  False

def removerAluno(matricula):
    aluno = alunoExiste(matricula)
    if aluno:
        banco_de_dados.remove(aluno)
        print('Aluno Removido Com Sucesso!')
    else:
        print('Matricula não Encontrada!')

def consultarAluno(matricula):
    aluno = alunoExiste(matricula)
    if aluno:
        print('---- DADOS DO ALUNO ----')
        print(f'Matricula: {aluno["matricula"]}')
        print(f'Nome: {aluno["nome"]}')
        print(f'Idade:{aluno["idade"]}')
        print(f'Curso: {aluno["curso"]}')
    else:
        print('Matricula não Encontrada!')

def menu():
    while True:
        print('---- BEM VINDO AO MENU ----')
        print('1 - Adicionar Aluno:')
        print('2 - Editar Aluno:')
        print('3 - Remover Aluno:')
        print('4 - Buscar Aluno:')
        print('5 - Listar Todos os Alunos:')
        print('6 - Sair do Sistema')
        opcao = input('Selecione uma Opção:')
        if opcao == '1':
            nome = input('Digite o nome:')
            idade = int(input('Digite a Idade:'))
            curso = input('Digite o Curso:')
            adicionarAluno(nome, idade, curso)

        elif opcao == '2':
            matricula = int(input('Digite a Matricula:'))
            nome = input('Digite o nome:')
            idade = int(input('Digite a Idade:'))
            curso = input('Digite o Curso:')
            editarAluno(matricula, nome, idade, curso)

        elif opcao == '3':
            matricula = int(input('Digite a Matricula:'))
            removerAluno(matricula)

        elif opcao == '4':
            matricula = int(input('Digite a Matricula:'))
            consultarAluno(matricula)

        elif opcao == '5':
            listarTodosAlunos()

        elif opcao == '6':
            break
        else:
            print('Opção Inválida!')

menu()







