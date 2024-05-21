import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3

#começar com tela com um botão e um entry (nome)- v1
#adicionar mais duas entrys (cpf e estado) e suas labels - v2
#mudar o fundo para uma imagem mais bonita, adicionar readme.txt explicando como usar - v3
#adicionar clicar no botão salva os 3 dados em um sqlite - v4
#Criar uma branch em que le um config.txt com uma lista de 5 estados possiveis separados por pular linha - x1
#Mudar o separador para ; e adicionar mais 5 estados - x2
#Voltar para main, criar outra branch e criar um dropdown com 3 opções (clt, mei, socio) - y1
#Voltar para main, Corrigir o bug da função de cpf - v5
#Merge de x com v - v6
#Adicionar verificação de CPF e de estado, com base na função cpf e na lista de estados .txt antes de adicionar no sqlite v7

#Cria conexção
connection = sqlite3.connect("teste.db")

#Cria o cursos e cria a tabela
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (Nome TEXT, Estado TEXT, Cpf INTEGER)")


def VerificarCPF(CPF):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais, o que tornaria o CPF inválido
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito_verif_1 = 0
    else:
        digito_verif_1 = 11 - resto
    
    # Verifica o primeiro dígito verificador
    if digito_verif_1 != int(cpf[9]):
        return False
    
    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito_verif_2 = 0
    else:
        digito_verif_2 = 11 - resto
    
    # Verifica o segundo dígito verificador
    if digito_verif_2 != int(cpf[10]):
        return False
    
    # Se passou por todas as verificações, o CPF é válido
    return True


    # Exemplo de uso
    cpf = input("Digite o CPF: ")
    if valida_cpf(cpf):
        print("CPF válido")
        else:
    print("CPF inválido")

def inserevalores(Nome, Estado, Cpf):
    #Insere linha na tabela
    cursor.execute("INSERT INTO Tabela1 VALUES ('"+Nome+"', '"+Estado+"','"+Cpf+"')")

def pegavalores():
    #Pega valores da tabela
    rows = cursor.execute("SELECT * FROM Tabela1").fetchall()
    print(rows)

def funcExemplo():
    print("Exemplo de funcao")
    
def Main():
    root = tkinter.Tk()
    root.title("Trabalho RAD")
    root.resizable(False, False)

    root.configure(background='black') 

    label = tkinter.Label(root, text="Cpf")
    label.pack()

    textoEntrada = tkinter.StringVar()
    e1 = tkinter.Entry(root)
    e1.bind('<Key>', lambda x:textoEntrada.set(e1.get()+x.char))
    e1.pack()
    
    label = tkinter.Label(root, text="Estado")
    label.pack()

    textoEntrada = tkinter.StringVar()
    e1 = tkinter.Entry(root)
    e1.bind('<Key>', lambda x:textoEntrada.set(e1.get()+x.char))
    e1.pack()

    label = tkinter.Label(root, text="Nome")
    label.pack()

    textoEntrada = tkinter.StringVar()
    e1 = tkinter.Entry(root)
    e1.bind('<Key>', lambda x:textoEntrada.set(e1.get()+x.char))
    e1.pack()

   
    test2 = tkinter.Button(root, text="Salvar")
    test2['command'] = inserevalores('Nome','Estado','Cpf')  #alterar para chamar outra função
    test2.pack()

    n = tkinter.StringVar()
    escolha = ttk.Combobox(root, textvariable = n)
    escolha.pack()
    escolha['values'] = ('CLT','MEI','Socio')
    
   

    root.iconify() #Minimiza a tela
    root.update()
    root.deiconify() #Maximiza a tela
    root.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs

Main()
