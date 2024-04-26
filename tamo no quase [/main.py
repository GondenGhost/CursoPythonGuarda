import tkinter as tk

def exisbir_menssagem():
    label.config(text='ola, mundo!')

janela = tk.tk()

label = tk.label(janela,text='bem-vindo!')

botao = tk.button(janela,text='clique aqui',command_menssagem)

label.pack()
botao.pack()

janela.mainloop()
