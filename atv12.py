turmas = int(input("Informe a quantidade de turmas:"))
alunos_total = 0

for i in range(turmas):
    alunos = int(input("Informe a quatidade de alunos das turmas:"))
    if alunos > 40:
        print("A turma tem mais de 40 alunos.")
    else:
        alunos_total += alunos
        media = alunos_total/turmas
        print(f"A media de alunos é: {media}")
