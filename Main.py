# Importação das bibliotecas necessárias
import easyocr
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF

# Criando leitor OCR (EasyOCR)
leitor_ocr = easyocr.Reader(['pt'])  # Define o idioma para português

# Função para selecionar arquivos (PDF e imagens)
def selecionar_arquivos():
    root = tk.Tk()
    root.withdraw()
    caminho_arquivos = filedialog.askopenfilenames(filetypes=[("Imagens e PDFs", "*.png; *.jpg; *.jpeg; *.pdf")])
    return list(caminho_arquivos)  # Retorna os caminhos selecionados

# Função para extrair texto de PDFs
def extrair_texto_pdf(caminho_pdf):
    texto = ""
    doc = fitz.open(caminho_pdf)
    for pagina in doc:
        texto += pagina.get_text() + "\n"  # Adiciona quebra de linha entre páginas
    return texto  

# Função para extrair texto de imagens usando EasyOCR
def extrair_texto_imagem(caminho_imagem):
    resultado = leitor_ocr.readtext(caminho_imagem, detail=0)  # Extrai apenas o texto, sem coordenadas
    return "\n".join(resultado)  # Junta os textos detectados em linhas

# Processamento dos arquivos
def processar_arquivos(arquivos):
    resultados = []  # Lista para armazenar os textos extraídos

    for arquivo in arquivos:
        if arquivo.lower().endswith(".pdf"):
            texto_extraido = extrair_texto_pdf(arquivo)
        elif arquivo.lower().endswith((".png", ".jpg", ".jpeg")):
            texto_extraido = extrair_texto_imagem(arquivo)
        else:
            texto_extraido = "Formato não suportado"

        # Adiciona os dados em um dicionário
        resultados.append({"Arquivo": os.path.basename(arquivo), "Texto Extraído": texto_extraido})

    return resultados

# Função para salvar em Excel
def salvar_em_excel(dados, nome_arquivo="texto_extraido.xlsx"):
    df = pd.DataFrame(dados)  # Cria um DataFrame
    df.to_excel(nome_arquivo, index=False)  # Salva em arquivo Excel
    print(f"\nOs textos foram salvos em '{nome_arquivo}'.")

# Início do processo
arquivos_selecionados = selecionar_arquivos()

if arquivos_selecionados:
    dados_extraidos = processar_arquivos(arquivos_selecionados)
    salvar_em_excel(dados_extraidos)
else:
    print("Nenhum arquivo foi selecionado.")
