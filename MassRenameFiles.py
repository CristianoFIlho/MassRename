import tkinter as tk
from tkinter import filedialog
import os
import glob
import shutil

def rename_files():
    folder_path = filedialog.askdirectory()
    file_type = file_type_entry.get()
    new_name = new_name_entry.get()

    if folder_path and file_type and new_name:
        files = glob.glob(os.path.join(folder_path, f"*{file_type}"))
        for file in files:
            new_file = os.path.join(folder_path, new_name.format(timestamp=int(time.time())))
            shutil.move(file, new_file)
        
        result_label.config(text="Arquivos renomeados com sucesso!")
    else:
        result_label.config(text="Por favor, preencha todos os campos.")

# Cria a janela principal
window = tk.Tk()
window.title("Renomear Arquivos em Massa")

# Cria os elementos da interface
folder_button = tk.Button(window, text="Selecionar Pasta", command=rename_files)
file_type_label = tk.Label(window, text="Tipo de Arquivo:")
file_type_entry = tk.Entry(window)
new_name_label = tk.Label(window, text="Novo Nome:")
new_name_entry = tk.Entry(window)
rename_button = tk.Button(window, text="Renomear", command=rename_files)
result_label = tk.Label(window, text="")

# Posiciona os elementos na janela
folder_button.pack()
file_type_label.pack()
file_type_entry.pack()
new_name_label.pack()
new_name_entry.pack()
rename_button.pack()
result_label.pack()

# Inicia o loop principal da interface
window.mainloop()