import os
import tfs_pdf_downloader
import tfs_pdf_extractor
import transcripts_repository

TEMP_FOLDER = "temp"
PDF_FOLDER = "pdf"
TIM_FERRIS_SHOW_ID = 1

tfs_pdf_downloader.download(TEMP_FOLDER, PDF_FOLDER)
transcripts_repository.clean_show_data(TIM_FERRIS_SHOW_ID)

files = os.listdir(PDF_FOLDER)
for file in files:
    episodeNumber = file.split('-')[0]
    print(f'{episodeNumber}: {file}')
    episodeId = transcripts_repository.save_episode(TIM_FERRIS_SHOW_ID, episodeNumber, file)
    episodeTalksList = tfs_pdf_extractor.extract_text(f"{PDF_FOLDER}/{file}")

    interventionNumber = 1
    for talk in episodeTalksList:
        transcripts_repository.save_episode_talk(episodeId, interventionNumber, talk.speaker, talk.speech)
        interventionNumber += 1



