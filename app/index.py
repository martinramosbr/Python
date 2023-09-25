# NOME: MARTINHO RAMOS DA CRUZ CORREIA FILHO
# CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS EAD


# VARIAVEIS DE ESCOPO
menu_principal = "-----MENU PRINCIPAL-----"
menu_professores = "*****[PROFESSORES] MENU DE OPERAÇÕES*****"
menu_estudantes = "*****[ESTUDANTES] MENU DE OPERAÇÕES*****"
menu_disciplinas = "*****[DISCIPLINAS] MENU DE OPERAÇÕES*****"
menu_turmas = "*****[TURMAS] MENU DE OPERAÇÕES*****"
menu_matriculas = "*****[MATRÍCULAS] MENU DE OPERAÇÕES*****"

menu_prin = ["Gerenciar estudantes", "Gerenciar profesores", "Gerenciar disciplinas", "Gerenciar turmas", "Gerenciar matrículas", "Sair"]
menu_sec = ["Incluir","Listar","Atualizar", "Excluir", "Voltar ao menu principal"]

p_opcao ="Informe a opção desejada: "
p_acao ="Informe a ação desejada: "

title_atualiza = "===== ATUALIZAÇÃO ====="
title_listagem = "===== LISTAGEM ====="

option_select = 0

alunos = []

#FUNÇÃO PARA CARREGAR O MENU INICIAL
def init_menu():
  global option_select
  i = 1
  print(menu_principal)

  for m in menu_prin:
    print(f"({i}) {m}")
    i+= 1

  option = int(input(p_opcao))
  option_select = option
  print_menu_sec(option)

#FUNÇÃO PARA CARREGAR O MENU DE AÇÕES 
def print_menu_sec(val):
  import os
  os.system('cls')
  if isinstance(val, int) and 0 < val <= 6: 
    if val == 1:
      i=1
      print(menu_estudantes)
      for ms in menu_sec:
        print(f"({i}) {ms}")
        i += 1

      option2 = int(input(p_acao))

    elif val == 2:
      # i=1
      # print(menu_professores)
      # for ms in menu_sec:
      #   print(f"({i}) {ms}")
      #   i += 1
      # option2 = int(input(p_acao))
      print("EM DESENVOLVIMENTO")
      
    elif val == 3:
      # i=1
      # print(menu_disciplinas)
      # for ms in menu_sec:
      #   print(f"({i}) {ms}")
      #   i += 1
      # option2 = int(input(p_acao))
      print("EM DESENVOLVIMENTO")

    elif val == 4:
      # i=1
      # print(menu_turmas)
      # for ms in menu_sec:
      #   print(f"({i}) {ms}")
      #   i += 1
      # option2 = int(input(p_acao))
      print("EM DESENVOLVIMENTO")

    elif val == 5:
      # i=1
      # print(menu_matriculas)
      # for ms in menu_sec:
      #   print(f"({i}) {ms}")
      #   i += 1
      # option2 = int(input(p_acao))
      print("EM DESENVOLVIMENTO")

    elif val == 6:
      quit()

    print_acao(option2)

  else:
    print("O valor digitado é inválido. Digite um valor válido! \n")
    init_menu()

#CARREGA E EXECUTA A AÇÃO SELECIONADA
def print_acao(val):
  global alunos
  import os
  os.system('cls')
  
  if val == 1:
    print("===== INCLUSÃO ===== \n")
    aluno = str(input("Informe o nome do estudante: "))
    input("Pressione ENTER para continuar.")
    inserir_aluno(aluno)
    print_menu_sec(option_select)

  elif val == 2:
    lista_alunos(val)

  elif val == 3:
    # print(title_atualiza)
    # print("Finalizando a aplicação...")
    print("EM DESENVOLVIMENTO")

  elif val == 4:
    print("EM DESENVOLVIMENTO")

  elif val == 5:
    init_menu()

  else:
    print(option_select)
    print_menu_sec(option_select)

#FUNÇÃO PARA INCLUIR ALUNO NA LISTA
def inserir_aluno(val):
  if type(val) == str:
    alunos.append(val)

#FUNÇÃO PARA PERCORRER A LISTA DE ALUNOS E IMPRIMIR NO CONSOLE
def lista_alunos(val):
  global alunos
  
  if val == 2:
    if alunos != []:
      print(title_listagem)
      i = 0
      while i < len(alunos):
        print(f"- {alunos[i]}")
        i += 1
      input("Pressione ENTER para continuar.")

    else:
      print("Não há estudantes cadastrados")

init_menu()
