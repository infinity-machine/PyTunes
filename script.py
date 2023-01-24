from pytube import YouTube
import os

yt = YouTube(str(input('ENTER URL...\n')))

extract = yt.streams.filter(only_audio = True).first()

out_file = extract.download(output_path = './tunage')

base, ext = os.path.splitext(out_file)

new_file = base + '.mp3'

os.rename(out_file, new_file)

print(yt.title + ' DOWNLOADED SUCCESSFULLY')
