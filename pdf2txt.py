import PyPDF2
import re
import conjuncoes as cj

# Abre o arquivo pdf
# lembre-se que para o windows você deve usar essa barra -> /
# lembre-se também que você precisa colocar o caminho absoluto
# não fiz nada disso pois inseri o arquivo no diretório
pdf_file = open('Versão Reduzidamil - Lucas Felpi.pdf', 'rb')

# Faz a leitura usando a biblioteca
read_pdf = PyPDF2.PdfFileReader(pdf_file)

# pega o numero de páginas
number_of_pages = read_pdf.getNumPages()
# print(number_of_pages)


# lê as páginas completas
for enem in range(2, number_of_pages):
    page = read_pdf.getPage(enem)

    # extrai apenas o texto
    page_content = page.extractText().lower()
    # print(page_content)

    # faz a junção das linhas
    parsed = ''.join(page_content)

    # separando apenas o texto da redação
    inicio = parsed.find('"')
    # print(inicio)
    final = parsed.rfind('"', inicio)
    # print(final)
    # print(parsed[inicio+1: final])
    parsed = parsed[inicio + 1: final]

    # eliminar as quebras de linhas
    parsed.replace('\n', ' ')
    # eliminando o caractere \xa0
    frases = parsed.split()
    parsed = ' '.join(frases)
    print(parsed)

    # separando as frases
    frases = parsed.split('.')
    for fr in frases:
        print(fr)

    # procurando as conjunções coordenativas
    for fr in frases:
        for conj in cj.coordenadas:
            conj[2] += len(re.findall(conj[1], fr))
            # print(f'A conjunção [{conj[0]:^20}] aparece {conj[2]:>3} vezes')
            # print(f'\t{fr}')

    # procurando as conjunções subordinativas
    for fr in frases:
        for conj in cj.subordinadas:
            conj[2] += len(re.findall(conj[1], fr))
            # print(f'A conjunção [{conj[0]:^20}] aparece {conj[2]:>3} vezes')
            # print(f'\t{fr}')

    # procurando as conjunções duvidosas
    for fr in frases:
        for conj in cj.duvidosas:
            conj[2] += len(re.findall(conj[1], fr))
            # print(f'A conjunção [{conj[0]:^20}] aparece {conj[2]:>3} vezes')
            # print(f'\t{fr}')

    # procurando as Função sintática duvidosa
    for fr in frases:
        for conj in cj.perigosas:
            conj[2] += len(re.findall(conj[1], fr))
            # print(f'A conjunção [{conj[0]:^20}] aparece {conj[2]:>3} vezes')
            # print(f'\t{fr}')

# Imprimindo os Resultados

print('Conjunções Coordenativas:\n-----------------------')
cj.coordenadas.sort()
for conj in cj.coordenadas:
    if conj[2] != 0:
        print(f'{conj[0]:30}{conj[2]} vezes')

print('\nConjunções Subordinativas:\n-----------------------')
cj.subordinadas.sort()
for conj in cj.subordinadas:
    if conj[2] != 0:
        print(f'{conj[0]:30}{conj[2]} vezes')

print('\nConjunções Duvidosas:\n-----------------------')
cj.duvidosas.sort()
for conj in cj.duvidosas:
    if conj[2] != 0:
        print(f'{conj[0]:30}{conj[2]} vezes')

print('\nFunção Sintática Duvidosa:\n-----------------------')
cj.perigosas.sort()
for conj in cj.perigosas:
    if conj[2] != 0:
        print(f'{conj[0]:30}{conj[2]} vezes')
