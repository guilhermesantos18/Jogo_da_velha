import tkinter as tk

# Configurações da janela principal, tamanho, titulo, configurações
# das linha, das colunas e da fonte
janela_principal = tk.Tk()
janela_principal.title('Jogo do Galo')
janela_principal.geometry('600x600')
janela_principal.grid_columnconfigure([0, 1, 2], minsize=200)
janela_principal.grid_rowconfigure([0, 1, 2], minsize=200)


# Definir os botões
btn_1 = tk.Button(text='1', width=20, height=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_2 = tk.Button(text='2', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_3 = tk.Button(text='3', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_4 = tk.Button(text='4', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_5 = tk.Button(text='5', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_6 = tk.Button(text='6', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_7 = tk.Button(text='7', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_8 = tk.Button(text='8', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_9 = tk.Button(text='9', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')

# Posicionar os botões na tela
btn_1.grid(row=1, column=0)
print(btn_1.winfo_x())
print(btn_1.winfo_y())

janela_principal.mainloop()
