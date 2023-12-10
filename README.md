# MassRename
Descrição

Este projeto é um renomeador de arquivos em massa que pode ser usado para renomear arquivos de um determinado tipo ou que atendam a um determinado critério. O projeto é escrito em Python e usa as bibliotecas os, glob e shutil.

Requisitos

Python 3.7+
Bibliotecas os, glob e shutil
Instalação

Para instalar o projeto, execute os seguintes comandos:

git clone https://github.com/[seu-usuário]/renomeador-de-arquivos-em-massa.git
cd renomeador-de-arquivos-em-massa
pip install -r requirements.txt
Uso

Para renomear arquivos, execute o seguinte comando:

python renomeador.py [pasta] [tipo] [novo_nome]
Onde:

[pasta] é o caminho para a pasta que contém os arquivos que deseja renomear.
[tipo] é o tipo dos arquivos que deseja renomear. Por exemplo, para renomear arquivos PDF, use .pdf.
[novo_nome] é o novo nome que deseja dar aos arquivos.
Por exemplo, para renomear todos os arquivos PDF na pasta /path/to/pdfs com o novo nome arquivo-{timestamp}.pdf, execute o seguinte comando:

python renomeador.py /path/to/pdfs .pdf arquivo-{timestamp}.pdf
Exemplo

Aqui está um exemplo de como usar o projeto:

# Importe as bibliotecas necessárias
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
Este código encontrará todos os arquivos PDF na pasta /path/to/pdfs e os renomeará com o novo nome arquivo-{timestamp}.pdf, onde {timestamp} é um número inteiro que representa o tempo atual.

Contribuições

Contribuições são bem-vindas. Para contribuir, faça o fork do projeto no GitHub e crie uma pull request com suas alterações.

Licença

Este projeto é licenciado sob a licença MIT.
