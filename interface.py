import tkinter as tk
from tkinter import filedialog
import data_process as dp

# ===== interface grafica =====
# Criar a interface grafica
root = tk.Tk()
root.title("Listagem de horas extra, subsidio de refeicao e trabalho noturno")

# Funcaes para selecao de arquivos
def select_input_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    output_file_path.delete(0, tk.END)
    output_file_path.insert(0, file_path)


# Caixas de selecao de arquivos de input
input_label1 = tk.Label(root, text="Arquivo de Horas: ")
#input_label1.pack()
input_label1.grid(row=0, column=0, pady=10)
input_file_path1 = tk.Entry(root)
#input_file_path1.pack()
input_file_path1.grid(row=0, column=1, pady=10)
input_file_path1.config(bg='#555555', fg='white')


input_button1 = tk.Button(root, text="Selecionar Arquivo", command=lambda: select_input_file(input_file_path1))
#input_button1.pack()
input_button1.grid(row=0, column=2, pady=10)


input_label2 = tk.Label(root, text="Arquivo de Subsidio de Refeicao: ")
#input_label2.pack()
input_label2.grid(row=10, column=0, pady=10)
input_file_path2 = tk.Entry(root)
#input_file_path2.pack()
input_file_path2.grid(row=10, column=1, pady=10)
input_file_path2.config(bg='#555555', fg='white')

input_button2 = tk.Button(root, text="Selecionar Arquivo", command=lambda: select_input_file(input_file_path2))
#input_button2.pack()
input_button2.grid(row=10, column=2, pady=10)

input_label3 = tk.Label(root, text="Arquivo de Trabalho Noturno: ")
#input_label3.pack()
input_label3.grid(row=20, column=0, pady=10)
input_file_path3 = tk.Entry(root)
#input_file_path3.pack()
input_file_path3.grid(row=20, column=1, pady=10)
input_file_path3.config(bg='#555555', fg='white')

input_button3 = tk.Button(root, text="Selecionar Arquivo", command=lambda: select_input_file(input_file_path3))
#input_button3.pack()
input_button3.grid(row=20, column=2, pady=10)

# Caixa de selecao de arquivo de output
output_label = tk.Label(root, text="Arquivo de Output: ")
#output_label.pack()
output_label.grid(row=30, column=0, pady=10)

output_file_path = tk.Entry(root)
#output_file_path.pack()
output_file_path.grid(row=30, column=1, pady=10)
output_file_path.config(bg='#555555', fg='white')

output_button = tk.Button(root, text="Selecionar Arquivo", command=select_output_file)
#output_button.pack()
output_button.grid(row=30, column=2, pady=10)

# vou levar esta parte mais para o fim #
# Botao para processar os dados
process_button = tk.Button(root, text="Processar Dados", command=dp.processar_dados)
#process_button.pack()
process_button.grid(row=32, column=0, pady=30)
process_button.config(height=2, width=15, bg='#555555', fg='white')

# criar um rodapé com o nome do autor e data e outra linha com o nome da aplicação
rodape = tk.Label(root, text="Desenvolvido por Carlos Sampaio, 2023")
rodape.grid(row=133, column=1, pady=15)

rodape2 = tk.Label(root, text="Para utilização exclusiva do")
#diminuir o tamanho da letra
rodape2.config(font=(8))
rodape2.grid(row=134, column=1)

rodape3 = tk.Label(root, text="Município de Montemor-o-Novo")
rodape3.config(font=(8))
rodape3.grid(row=135, column=1)

# botão para sair da aplicação
sair = tk.Button(root, text="Sair", command=root.destroy)
sair.grid(row=32, column=2, pady=30)
sair.config(height=2, width=10)

# tamanho da janela
root.geometry("640x480")
# esquema de cores da aplicação. tema escuro
root.tk_setPalette(background='#333333', foreground='white', activeBackground='#555555', activeForeground='white')