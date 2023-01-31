import os
import sys
import tfs_pdf_downloader
import tfs_pdf_extractor
import transcripts_repository

TEMP_FOLDER = "temp"
PDF_FOLDER = "pdf"
#tfs_pdf_downloader.download(TEMP_FOLDER, PDF_FOLDER)

files = os.listdir(PDF_FOLDER)
for file in files:
    episodeNumber = file.split('-')[0]
    print(f'{episodeNumber}: {file}')
    transcripts_repository.save_episode(episodeNumber, file)
    episodeTalksList = tfs_pdf_extractor.extract_text(f"{PDF_FOLDER}/{file}")

    interventionNumber = 1
    for talk in episodeTalksList:
        transcripts_repository.save_episode_talk(1, interventionNumber, talk.speaker, talk.speech)
        interventionNumber += 1



