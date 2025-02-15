import tkinter as tk
from tkinter import *

class Tela:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Minha Primeira janela')
        self.janela.geometry('300x200+550+100')
        self.janela['bg'] = 'lightblue'
        self.janela.resizable(width=False, height=False)


        self.nome1 = tk.Label(self.janela, text='Entrar no Sistema', foreground='black', background='lightblue', font='Arial 12 bold')
        self.nome1.pack()
        self.botao1 = tk.Button(self.janela, text='Entrar',foreground='blue', background='lightgreen', width=10, height=2, font='verdana 12 bold')
        self.botao1.pack()
        self.nome1 = tk.Label(self.janela, text='Sair do Sistema', foreground='black', background='lightblue',
                              font='Arial 12 bold')
        self.nome1.pack()
        self.botao2 = tk.Button(self.janela, text='Sair', background='lightpink', width=10, height=2, font='verdana 12 bold')
        self.botao2.pack()



janela = tk.Tk()
objeto =Tela(janela)
janela.mainloop()
