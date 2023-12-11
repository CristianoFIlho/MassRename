import os
import glob
import shutil

# Defina a pasta que contém os arquivos que deseja renomear
pasta = "/path/to/pdfs"

# Defina o tipo dos arquivos que deseja renomear
tipo = ".pdf"

# Defina o novo nome que deseja dar aos arquivos
novo_nome = "arquivo-{timestamp}.pdf"

# Encontre todos os arquivos do tipo especificado
arquivos = glob.glob(os.path.join(pasta, f"*{tipo}"))

# Renomeie os arquivos
for arquivo in arquivos:
    novo_arquivo = os.path.join(pasta, novo_nome.format(timestamp=int(time.time())))
    shutil.move(arquivo, novo_arquivo)