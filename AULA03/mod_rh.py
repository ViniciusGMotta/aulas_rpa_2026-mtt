# mod_rh.py

def cadastrar_colaborador(nome, cargo, salario):
    colaborador = {"nome": nome, "cargo": cargo, "salario": salario}
    return colaborador


def exibir_colaboradores(lista_colaboradores):
    for colaborador in lista_colaboradores:
        print("Nome:", colaborador["nome"])
        print("Cargo:", colaborador["cargo"])
        print("Salário: R$", colaborador["salario"])
        print("------------------------")