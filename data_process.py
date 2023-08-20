import pandas as pd
import interface as itf

class Trabalhador:
    def __init__(self, nr, nome):
        self.nr = nr
        self.nome = nome
        self.prims = []
        self.segs = []
        self.sab = []
        self.fer = []
        self.dom = []
        self.subref = []
        self.trabnot = []

#retirado da funcao para nao dar erro
trabalhadores = {}

# criar função para ordenar a biblioteca de trabalhadores
def ordenar_trabalhadores():
    # ordenar os trabalhadores por nome
    trabalhadores_ordenados = sorted(trabalhadores.items(), key=lambda x: x[1].nome)
    # limpar a lista de trabalhadores
    trabalhadores.clear()
    # adicionar os trabalhadores ordenados à lista de trabalhadores
    for trabalhador in trabalhadores_ordenados:
        trabalhadores[trabalhador[0]] = trabalhador[1]


# Funcao para processar os dados com base nos arquivos selecionados
def processar_dados():
    input_file_paths = [itf.input_file_path1.get(), itf.input_file_path2.get(), itf.input_file_path3.get()]
    output_file = itf.output_file_path.get()

    #trabalhadores = {}

    for idx, input_file in enumerate(input_file_paths):
        if idx == 0:
            df = pd.read_csv(input_file, sep='|', header=None, encoding='latin-1')
            for index, row in df.iterrows():
                # Seu codigo de processamento de horas...
                nr = row[1]  # Numero do trabalhador
                nome = row[2]  # Nome do trabalhador
                
                # Verificar se o trabalhador ja existe no dicionario
                if nr in trabalhadores:
                    trabalhador = trabalhadores[nr]
                else:
                    trabalhador = Trabalhador(nr, nome)
                    trabalhadores[nr] = trabalhador
                
                # Adicionar as horas de acordo com o tipo
                tipo_horas = row[14]
                quantidade_horas = row[18]
                
                if tipo_horas == 41:
                    trabalhador.prims.append(quantidade_horas)
                elif tipo_horas == 42:
                    trabalhador.segs.append(quantidade_horas)
                elif tipo_horas == 43:
                    trabalhador.sab.append(quantidade_horas)
                elif tipo_horas == 44:
                    trabalhador.fer.append(quantidade_horas)
                elif tipo_horas == 45:
                    trabalhador.dom.append(quantidade_horas)
        
        # processamento de subsidio de refeicao
        elif idx == 1:
            dfs = pd.read_csv(input_file, sep='|', header=None, encoding='latin-1')
            for index, row in dfs.iterrows():
                # Seu codigo de processamento de subsidio de refeicao...
                nr = row[1]  # Numero do trabalhador
                nome = row[2]  # Nome do trabalhador
                subref = row[15]  # Subsidio de refeicao
                
                # Verificar se o trabalhador ja existe no dicionario
                if nr in trabalhadores:
                    trabalhador = trabalhadores[nr]
                else:
                    trabalhador = Trabalhador(nr, nome)
                    trabalhadores[nr] = trabalhador
                #trabalhadores[nr] = trabalhador    
                trabalhador.subref.append(subref)
                
        #processamento do trabalho noturno
        elif idx == 2:
            dft = pd.read_csv(input_file, sep='|', header=None, encoding='latin-1')
            for index, row in dft.iterrows():
                # Seu codigo de processamento de trabalho noturno...
                nr = row[1]  # Numero do trabalhador
                nome = row[2]  # Nome do trabalhador
                trabnot = row[15]  # Trabalho noturno
                
                # Verificar se o trabalhador ja existe no dicionario
                if nr in trabalhadores:
                    trabalhador = trabalhadores[nr]
                else:
                    trabalhador = Trabalhador(nr, nome)
                    trabalhadores[nr] = trabalhador
                #trabalhadores[nr] = trabalhador    
                trabalhador.trabnot.append(trabnot)

        
    # Ordenar os trabalhadores por nome
    ordenar_trabalhadores()

    # Exportar para um novo CSV
    output_data = []

    for nr, trabalhador in trabalhadores.items():
        output_data.append([trabalhador.nr, trabalhador.nome, trabalhador.prims, trabalhador.segs, trabalhador.sab, trabalhador.fer, trabalhador.dom, trabalhador.subref, trabalhador.trabnot])

    #output_df = pd.DataFrame(output_data, columns=['Nr', 'Nome', 'Primeiras', 'Seguintes', 'Sabado', 'Feriado', 'Domingo', 'SubRef', 'TrabNot'])
    #output_df.to_csv('output.csv', index=False)
    #output_df.to_csv(itf.output_file_path.get()+'.csv', index=False)

    # Exportar para um ficheiro XLSX
    output_df2 = pd.DataFrame(output_data, columns=['Nr', 'Nome', 'Primeiras', 'Seguintes', 'Sabado', 'Feriado', 'Domingo', 'SubRef', 'TrabNot'])
    #output_df2.to_excel(itf.output_file_path.get(), index=False)


    try:
        output_df2.to_excel(itf.output_file_path.get(), index=False)
        itf.tk.messagebox.showinfo("Sucesso", "Listagem processada com sucesso! \n A aplicação irá ser encerrada.")
        itf.root.quit()
    except Exception as e:
        itf.tk.messagebox.showerror("Erro", "Ocorreu um erro ao processar a listagem. \n")
        itf.input_file_path1.delete(0, itf.tk.END)
        itf.input_file_path2.delete(0, itf.tk.END)
        itf.input_file_path3.delete(0, itf.tk.END)
        itf.output_file_path.delete(0, itf.tk.END)
