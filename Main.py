# Nesta etapa, estou importando as bibliotecas necessárias para fazer todo o código funcionar.
import easyocr
import pandas
import os
import tkinter as tk
from tkinter import filedialog
import PyPDF2
import fitz  # PyMuPDF


# Adicionando as funções que usarei para realizar a leitura da imagem
def selecionar_imagens():
    root = tk.Tk()
    root.withdraw()
    caminho_imagens = filedialog.askopenfilenames(filetypes=[("Imagens", "*.png; *.jpg; *.jpeg; *.pdf")]) #aqui, podemos alterar para o código receber as imagens que desejamos
    return caminho_imagens # retornamos o nosso caminho de imagens

def selecionar_pdf(caminho_pdf):
    texto = ""
    doc = fitz.open(caminho_pdf)
    for pagina in doc:
        texto += pagina.get_text() # Aqui, é extraído o texto de cada imagem
    return texto  

def processamento(arquivos):
    for arquivos in arquivos:
        if arquivos.lower().endswith(('png', 'jpg', 'jpeg')):
            resultado = leitura.readtext(arquivo)
            for item in resultado:
                print(f"Texto extraído da imagem: {item[1]}")
        elif arquivos.lower().endswhith('pdf'):
            texto_pdf = selecionar_pdf(arquivo)
            print(f"Texto extraído do PDF: \n{texto_pdf}")
        else:
            print(f"Arquivo {arquivos} não suportado")


