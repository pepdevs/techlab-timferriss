import os

files = os.listdir('pdf')
for file in files:
    episodeNumber = file.split('-')[0]
    print(f'{episodeNumber}: {file}')