import PyPDF2
import os
from tkinter import filedialog


merger = PyPDF2.PdfMerger()
diretorio = filedialog.askdirectory()
arquivos = os.listdir(diretorio)
arquivos.sort()

for arquivo in arquivos:
    if ".pdf" in arquivo:
        merger.append(f"{diretorio}/{arquivo}")

salvar = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", ".pdf")])
with open(salvar, "wb") as pdfmesclado:
    merger.write(pdfmesclado)



