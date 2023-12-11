# MassRename
Descrição

Este projeto é um renomeador de arquivos em massa que pode ser usado para renomear arquivos de um determinado tipo ou que atendam a um determinado critério. O projeto é escrito em Python e usa as bibliotecas os, glob e shutil.

Requisitos

Python 3.7+
Bibliotecas os, glob e shutil
Instalação

Para instalar o projeto, execute os seguintes comandos:

git clone https://github.com/CristianoFIlho/MassRename.git 
cd MassRename
pip install -r requirements.txt
Uso

Para renomear arquivos, execute o seguinte comando:

python MassRenameFiles.py [pasta] [tipo] [novo_nome]
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

# Branches no desenvolvimento

* **Main:** Esta é a branch principal do projeto, que contém o código que está em produção.
* **Develop:** Esta é a branch de desenvolvimento, que contém o código que está sendo desenvolvido, mas ainda não está pronto para ser lançado.
* **Feature branches:** Estas são branches temporárias que são criadas para desenvolver novas funcionalidades.

# Commits Semânticos

Este projeto usa commits semânticos para padronizar as mensagens de commit. Para fazer um commit semântico, use um dos seguintes prefixos no início da mensagem de commit:


- ✨ `:sparkles:`: para adicionar uma nova funcionalidade ao código.
- 🐛 `:bug:`: para corrigir um bug no código.
- 📚 `:books:`: para adicionar ou atualizar a documentação.
- 🚀 `:rocket:`: para melhorar o desempenho ou a eficiência do código.
- 🎨 `:art:`: para melhorar a estrutura ou a aparência do código.
- 🚧 `:construction:`: para indicar que o código está em progresso ou em desenvolvimento.
- 📦 `:package:`: para adicionar ou atualizar dependências do projeto.
- ♻️ `:recycle:`: para refatorar o código, melhorando sua estrutura ou legibilidade.
- 🚨 `:rotating_light:`: para corrigir problemas de segurança no código.
- 🌐 `:globe_with_meridians:`: para alterações relacionadas à internacionalização ou localização.
- ⚡️ `:zap:`: para melhorar o desempenho do código.



Licença

Este projeto é licenciado sob a licença MIT.
