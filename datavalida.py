data = input()

dia = int(data[0:2])
mes = int(data[2:4])
ano = int(data[4:8])

##verificação de ano bissexto
ano_bissexto = False
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 ==0):
    ano_bissexto = True

##verificação da validade da data
data_valida = True
##verificação do dia
if dia < 1 or dia > 31:
    data_valida = False
##verificação do mês
if mes < 1 or mes > 12:
    data_valida = False
##verificação de fevereiro em ano não bissexto
if mes == 2 and not ano_bissexto and dia > 28:
    data_valida = False
##verificação dos meses com 30 dias
if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
    data_valida = False
print(data_valida)
