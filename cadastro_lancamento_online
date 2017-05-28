""" REMOVIDOS POR NÃO SER EFICAZ LANÇAR ONLINE DIRETO
    (LEVA TEMPO E A AUTENTICAÇÃO EXPIRA DEPOIS DE ALGUNS MINUTOS DE EXECUÇÃO)

    PARA UTILIZÁ-LAS, COPIAR AMBAS PARA O ARQUIVO FREQUENCIA.PY E TIRAR O
    COMENTÁRIO DAS CHAMADAS PRA ELA"""


def cadastraCodigo(colunaMatriculas, colunaCodigos):
    a = 0
    print "CADASTRAR CODIGO"
    presenca = raw_input("Lancar presenca apos cadastrar? (S/n): ")
    presenca = presenca.upper()

    if presenca != "N":
        presenca = True
    else:
        presenca = False

    while True:
        while True:
            try:
                matricula = raw_input("Digite sua matricula: ")
                matricula = matricula.upper()  # maiuscula
                a = sheet.find(matricula)
                if a.col != colunaMatriculas:
                    print "Matricula nao encontrada"
                else:
                    print "Matricula encontrada"
                    break

            except (gspread.exceptions.CellNotFound):
                print "Matricula nao encontrada"

            except (NameError):
                print "Sistema offline. Utilizar cadastraOffline"
                break
        linha = a.row
        codigo = leCodigo()
        sheet.update_cell(linha, colunaCodigos, codigo)
        print "Codigo cadastrado\n"
        if presenca:
            lancaPresenca(str(codigo))
        print "CADASTRAR CODIGO"


def lancaPresenca(codigo=False):  # parametro pra poder chamar do cadastro
    dia = obtemDia()
    breaksoon = False

    if codigo is not False:
        breaksoon = True

    while True:
        print "\nLANCAR PRESENCA"
        if (breaksoon is False):
            codigo = str(leCodigo())
        print "Buscando codigo na planilha"

        try:
            coluna = sheet.find(dia).col
            linha = sheet.find(codigo).row

        except (gspread.exceptions.CellNotFound):
            print "Codigo ou dia invalido"

        except (NameError):
            salvaTxtNaoLancadas(codigo, dia)
            print "Presenca lancada no txt"
            print "Presenca NAO lancada na planilha"

        else:
            salvaTxtLancadas(codigo, dia)
            print "Presenca lancada no txt"
            sheet.update_cell(linha, coluna, 1)
            print "Presenca lancada na planilha\n"

        if breaksoon:
            break
        again = raw_input("Inserir outra? (S/n): ")
        again = again.upper()
        if again == "N":
            break
