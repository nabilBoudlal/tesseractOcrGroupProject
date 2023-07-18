## Group Project per OCR su documenti storici 

Questa repository contiene un progetto focalizzato sull'utilizzo di Tesseract OCR per crafting e riconoscimento ottico dei caratteri.
Il progetto mira a estrarre il testo dalle immagini utilizzando Tesseract OCR e fornisce un'interfaccia conveniente per eseguire operazioni OCR su più immagini.

### Funzionalità

- Elaborazione di immagini in batch: il progetto supporta l'elaborazione di più immagini in batch, consentendo operazioni OCR efficienti su un gran numero di immagini.
- Esportazione dei risultati: i risultati del testo estratto possono essere esportati in vari formati come testo semplice,per ulteriori analisi o integrazione con altri sistemi.

### Installazione

1. Clona il repository:

```
git clone https://github.com/nabilBoudlal/tesseractOcrGroupProject.git
```

2. Installa le dipendenze richieste:

```
pip install -r requirements.txt
```

3. Scarica e installa Tesseract OCR:

   - Windows: Scarica l'installer dal [sito web di Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) e segui le istruzioni di installazione.
   - macOS: Installa Tesseract OCR usando Homebrew eseguendo il seguente comando:

   ```
   brew install tesseract
   ```

   - Linux: Installa Tesseract OCR usando il gestore di pacchetti della tua distribuzione. Ad esempio, su Ubuntu, esegui:

   ```
   sudo apt-get install tesseract-ocr
   ```

### Utilizzo

1. Posiziona le immagini che desideri elaborare nella cartella "input".
2. Esegui lo script principale:

```
python main.py .\input\ .\results\

```
3. I risultati del testo estratto verranno salvati nella cartella "result" secondo il formato di esportazione specificato.

### Licenza

Questo progetto è distribuito con licenza [MIT License](LICENSE).
