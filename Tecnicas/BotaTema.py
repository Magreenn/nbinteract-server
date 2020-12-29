from bs4 import BeautifulSoup

with open('Modelo.html', encoding="utf8") as modelo_file:
    modelo = BeautifulSoup(modelo_file, 'lxml')
with open(input("Escreva o nome do arquivo base .html:"), encoding="utf8") as base_file:
    base = BeautifulSoup(base_file, 'lxml')
    conteudo = base.body
    modelo.html.append(conteudo)
with open(input("Escreva o nome do arquivo final .html:"), encoding="utf8", mode="w") as final_file:
    final_file.write(modelo.prettify())

