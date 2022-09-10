import pandas as pd 

def update_nota_by_grupo(dataset, grupo, nota):
    dataset["Nota"].loc[dataset["Grupo"] == grupo] = nota

def search_aluno_by_matricula(dataset, matricula):
    return dataset.loc[dataset["Matricula"] == matricula]

def add_grupo_to_aluno(dataset, grupo, matricula):
    dataset["Grupo"].loc[dataset["Matricula"] == matricula] = grupo

def write_to_csv(dataset):
    dataset.to_csv('results.csv', index=False)

def print_aluno(dataset, matricula):
    aluno = search_aluno_by_matricula(dataset, matricula)
    print(aluno)

def menu(dataset):
    print("Bem vindo ao nota atualization 2000!")
    print("1 - Atualizar nota do grupo")
    print("2 - Busca aluno")
    print("3 - Mostrar todos os alunos")
    print("4 - Salvar arquivo")
    print("5 - Adicionar aluno ao grupo")
    print("0 - Sair")

    x = int(input("Digite a opção desejada: "))

    if (x == 1):
        matricula = input("Digite a matricula do aluno: ")
        grupo = input("Digite o grupo do aluno: ")
        nota = input("Digite a nota do grupo: ")
        add_grupo_to_aluno(dataset, grupo, matricula)
        update_nota_by_grupo(dataset, grupo, nota)
    
    if (x == 2):
        matricula = input("Digite a matricula do aluno")
        print_aluno(dataset, matricula)
    
    if (x == 3):
        print(dataset)
        print("\n\n")
    
    if (x == 4):
        write_to_csv(dataset)
    
    if (x == 5):
        matricula = int(input("Digite a matricula do aluno: \n"))
        grupo = int(input("Digite o grupo do aluno: \n"))
        add_grupo_to_aluno(dataset, grupo, matricula)

    if (x == 0):
        exit()

def main ():
    dataset = pd.read_csv("alunos.csv", header=None, names=["Nome", "Matricula", "Grupo", "Nota"])
    while True:
        menu(dataset)

if __name__ == '__main__':
    main()
