from pytube import YouTube
import os
import sys
import pyfiglet
    
def intro():
    banner = pyfiglet.figlet_format("PyTunes", font = "isometric3" )
    print(banner)
    print('PYTUNES 2023 SHLERM INDUSTRIAL SOLUTIONS CORP')

def main(): 
    url = input('AWAITING URL...("EXIT" TO TERMINATE)\n')
    if url.lower() == 'exit':
        print('SAYONARA!')
        sys.exit()

    yt = YouTube(str(url))
    extract = yt.streams.filter(only_audio = True).first()
    out_file = extract.download(output_path = './tunage')
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(yt.title + ' DOWNLOADED SUCCESSFULLY')
    print('GROOVE ON SOUL BROTHER!')
    main()

intro()
main()
 