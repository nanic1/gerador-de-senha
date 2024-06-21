from customtkinter import CTkTextbox, CTkButton, CTkEntry
from tkinter import *
from random import choice
from pyperclip import copy
import io

branco = "#e8e5dc"

tela = Tk()
tela.geometry("350x300")
tela.title("Gerador de senha")
tela.configure(bg=branco)
tela.resizable(width=False, height=False)
tela.iconbitmap("cadeado.ico")
senhaString = StringVar()


def gerarSenha():
    lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
              'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
              'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2',
              '3', '4', '5', '6', '7', '8', '9', '0', '!',
              '@', '#', '$', '%', '^', '&', '*', '(', ')']
    
    senha = ""
    for x in range(1, 30):
        senha = senha + choice(lista1)
    senhaString.set(senha)

tituloLabel = Label(tela, text="Gerador de senha", font=("Fixedsys 20"), bg=branco)
tituloLabel.pack(padx=10, pady=10)

labelentry = CTkEntry(tela, height=50, textvariable=senhaString, width=250)
labelentry.pack(padx=10, pady=10)

gerarButton = CTkButton(tela, text="Gerar senha", font=("Verdana", 20), command=gerarSenha)
gerarButton.pack(padx=10, pady=10)

tela.mainloop()