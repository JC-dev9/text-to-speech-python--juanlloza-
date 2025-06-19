from gtts import gTTS
import sys
import os

def save_text_to_mp3(text):
    # Salva o arquivo no mesmo diretório do script
    filename = os.path.join(os.path.dirname(__file__), "temp_ptpt.mp3")
    tts = gTTS(text, lang='pt', tld='pt')
    tts.save(filename)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        save_text_to_mp3(sys.argv[1])
    else:
        print("Texto não fornecido.")
