import os
import pymupdf
import json

def exportar_metadados(arquivo):

    nome_arquivo = str(arquivo)
    nome_arquivo_pdf = nome_arquivo + ".pdf"
    doc = pymupdf.open(f"arquivos/{nome_arquivo_pdf}")
    
    for page in doc: 
        pdf_content = page.get_text()
    
    metadados = doc.metadata

    with open(f'metadados.json', 'w', encoding='utf-8') as file:
        metadadosA = json.dump(metadados, file, indent=4)

    with open(f'texto_arquivo.json', 'w', encoding='utf-8') as file:
        textoA = json.dump({'texto' : f'{pdf_content}'}, file, indent=4)
    
    with open('metadados.json', 'r') as f:
        data1 = json.load(f)

    with open('texto_arquivo.json', 'r') as f:
        data2 = json.load(f)

    data1.update(data2)

    with open(f'arquivos/{nome_arquivo}.json', 'w', encoding='utf-8') as file:
        json.dump(data1, file, indent=4)

    os.remove('metadados.json')
    os.remove('texto_arquivo.json')
