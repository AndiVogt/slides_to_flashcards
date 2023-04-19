
from PyPDF2 import PdfReader
import os

# Funktion, die die Dateipfade aller Dateien im angegebenen Ordner zurückgibt
def get_file_paths(folder_path):
    files = []
    for file in os.listdir(folder_path):
        filename = os.fsdecode(file)
        file_path = os.path.join(folder_path, filename)
        files.append(file_path)
    return files

# Funktion, die den Inhalt aller Seiten in allen PDF-Dateien im übergebenen Dateipfad zurückgibt
def get_slide_content(file_paths):
    content = list()
    for slide in file_paths:
        single_content = "" 
        with open(slide, "r") as file: 
            pdf = PdfReader(slide)
            pages = len(pdf.pages) 
            for page in range(pages): # Für jede Seite in der PDF-Datei
                pageObj = pdf.pages[int(page)]
                single_content += pageObj.extract_text() 
            content.append(single_content) # Fügt den Inhalt der aktuellen PDF-Datei zur Liste des gesamten Inhalts hinzu
    return content

