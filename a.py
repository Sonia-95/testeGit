import tkinter as tk
from tkinter import *

class Tela:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Minha Primeira janela')
        self.janela['background']='lightblue'
        self.janela.geometry('300x200+550+100')
        self.nome1 = tk.Label(self.janela,width =10, text='label com padding x,y', cursor='dotbox', relief='groove', padx=25, pady=25)
        self.nome1.pack()
        self.botao=tk.Button(self.janela,text='botão com padding x,y', padx=80, pady=50)
        self.botao.pack()

janela = tk.Tk()
objeto =Tela(janela)
janela.mainloop()