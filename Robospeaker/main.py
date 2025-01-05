import os

if __name__== '__main__':
    print("Welcome to robospeaker 1.1. created by Khushal")
    while (True):
        x=input ("Enter what u want to speak: ")
        if (x=="q"):
              os.system("espeak '{bye bye friend}'")
              break
        command=f"espeak '{x}'"# install espeak on kali by sudo apt-get espeak
        os.system(command)