import os
import glob
from PIL import Image
import pytesseract


def text_recognition():
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    # Percorso della cartella "crafted"
    crafted_folder = "crafted/"

    # Lista delle sottodirectory all'interno di "crafted"
    subdirectories = [name for name in os.listdir(crafted_folder) if os.path.isdir(os.path.join(crafted_folder, name))]

    # Itera su ogni sottodirectory
    for subdirectory in subdirectories:
        # Percorso completo della sottodirectory
        subdirectory_path = os.path.join(crafted_folder, subdirectory)

        # Percorso della cartella "image_crops" all'interno della sottodirectory
        image_crops_folder = os.path.join(subdirectory_path, "image_crops")

        # Lista dei percorsi completi di tutte le immagini nella cartella "image_crops"
        image_paths = glob.glob(os.path.join(image_crops_folder, '*.png'))
        image_paths = sorted(image_paths)

        # Percorso del file di output in cui verranno scritti i risultati
        output_file = f'results/{subdirectory}.txt'

        # Inizializza una stringa per memorizzare i risultati
        results = ""

        # Itera su ogni immagine nella cartella "image_crops"
        for image_path in image_paths:
            # Leggi l'immagine
            img = Image.open(image_path)

            # Esegui l'OCR sull'immagine
            custom_config = r'--psm 7'  # Configurazione personalizzata per il rilevamento del testo
            text = pytesseract.image_to_string(img, config=custom_config)

            # Aggiungi il risultato alla stringa dei risultati
            results += text + " "

        # Scrivi i risultati sul file di output
        with open(output_file, 'w') as file:
            file.write(results)
