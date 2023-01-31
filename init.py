import os
import sys
import tfs_pdf_downloader
import tfs_pdf_extractor
import transcripts_repository

TEMP_FOLDER = "temp"
PDF_FOLDER = "pdf"
tfs_pdf_downloader.download(TEMP_FOLDER, PDF_FOLDER)

files = os.listdir(PDF_FOLDER)
for file in files:
    episodeNumber = file.split('-')[0]
    print(f'{episodeNumber}: {file}')
    tfs_pdf_extractor.extract_text(f"{PDF_FOLDER}/{file}")



