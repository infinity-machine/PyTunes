from pytube import YouTube
import os
import pyfiglet

result = pyfiglet.figlet_format("PyTunes", font = "isometric3" )
print(result)
print('SHLERMS INDUSTRIAL SOLUTIONS CORP')

yt = YouTube(str(input('AWAITING URL...\n')))

extract = yt.streams.filter(only_audio = True).first()
out_file = extract.download(output_path = './tunage')
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'

os.rename(out_file, new_file)

print(yt.title + ' DOWNLOADED SUCCESSFULLY')
