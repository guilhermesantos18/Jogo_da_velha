import tkinter as tk
from tkinter import messagebox

flag = 0

# Configurações da janela principal
janela_principal = tk.Tk()
janela_principal.title('Jogo do Galo')


# Verificar o Vencedor
def Vencedor():
    if btn_1['text'] == 'X' and btn_2['text'] == 'X' and btn_3['text'] == 'X':
        print('O jogador X Venceu!')
    elif btn_1['text'] == 'O' and btn_2['text'] == 'O' and btn_3['text'] == 'O':
        print('O jogador O Venceu!')
    elif btn_1['text'] == 'X' and btn_4['text'] == 'X' and btn_7['text'] == 'X':
        print('O jogador X Venceu!')
    elif btn_1['text'] == 'O' and btn_4['text'] == 'O' and btn_7['text'] == 'O':
        print('O jogador O Venceu!')


# Colocar o texto nos botões X ou O e mostrar mensagem de erro casa pressione no mesmo sítio mais de uma vez
def main(button):
    global flag
    if flag == 0 and button['text'] == '':
        button['text'] = 'X'
        flag = 1
    elif flag == 1 and button['text'] == '':
        button['text'] = 'O'
        flag = 0
    else:
        messagebox.showerror(title='Jogo da Velha', message='Não pressione no mesmo sítio mais de uma vez...')
    Vencedor()


# Definir os botões
btn_1 = tk.Button(text='', width=10, height=5, bg='white', command=lambda: main(btn_1))
btn_2 = tk.Button(text='', width=10, height=5, bg='white', command=lambda: main(btn_2))
btn_3 = tk.Button(text='', width=10, height=5, bg='white', command=lambda: main(btn_3))
btn_4 = tk.Button(text='', width=10, height=5, bg='white', command=lambda: main(btn_4))
btn_5 = tk.Button(text='', width=10, height=5, bg='white', command=lambda: main(btn_5))
btn_6 = tk.Button(text='', width=10, height=5, bg='white', command=lambda: main(btn_6))
btn_7 = tk.Button(text='', width=10, height=5, bg='white', command=lambda: main(btn_7))
btn_8 = tk.Button(text='', width=10, height=5, bg='white', command=lambda: main(btn_8))
btn_9 = tk.Button(text='', width=10, height=5, bg='white', command=lambda: main(btn_9))

# Posicionar os botões na tela
btn_1.grid(row=0, column=0)
btn_2.grid(row=0, column=1)
btn_3.grid(row=0, column=2)

btn_4.grid(row=1, column=0)
btn_5.grid(row=1, column=1)
btn_6.grid(row=1, column=2)

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)


janela_principal.mainloop()
