import os
from datetime import datetime

# Solicitar informações ao usuário
file_name = input("Digite o nome do arquivo: ")
post_title = input("Digite o título do post: ")
description = input("Digite uma descrição curta: ")
tags = input("Digite as tags separadas por vírgula: ")

# Obter a data e hora atual
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Criar o conteúdo do arquivo
file_content = f"""---
title: {post_title}
date: {current_datetime}
description: {description}
tags: [{tags}]
---

# {post_title}
"""

# Nome do arquivo com extensão .md
file_name = f"{file_name}.md"

# Caminho completo para o arquivo na pasta raiz
file_path = os.path.join(os.getcwd(), file_name)

# Escrever o conteúdo no arquivo
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"Arquivo '{file_name}' criado com sucesso na pasta raiz.")
