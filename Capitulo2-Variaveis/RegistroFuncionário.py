nome=input("Digite um funcionário: ")
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a qtde de funcionários: "))
mediaHoras=float(input("Digite a média de horas: "))

print(nome + " trabalha na empresa " + empresa)
print("Instituição com ", qtde_funcionarios, " funcionarios.")
print("A média de horas é de: " + str(mediaHoras))

print("==============Verifique os tipos de dados abaixo:==============")

print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaHoras] é: ",type(mediaHoras))
