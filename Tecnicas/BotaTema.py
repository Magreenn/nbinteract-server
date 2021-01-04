from bs4 import BeautifulSoup

arquivo_inicial = input("Escreva o nome do arquivo fonte:")
arquivo_final = input("Escreva o nome do arquivo de destino:")

with open('Modelo.html', encoding="utf8") as modelo_file:
    modelo = BeautifulSoup(modelo_file, 'lxml')
with open(f'{arquivo_inicial}.html', encoding="utf8") as base_file:
    base = BeautifulSoup(base_file, 'lxml')
    conteudo = base.body
    titulo = modelo.title
    titulo.string = arquivo_final
    modelo.html.append(conteudo)
with open(f'{arquivo_final}.html', encoding="utf8", mode="w") as final_file:
    final_file.write(modelo.prettify())