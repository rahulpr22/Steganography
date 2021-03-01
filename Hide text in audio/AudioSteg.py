import wave
import numpy as np
import math,re
import simpleaudio as sa

def playAudio(audio):
    wave_obj = sa.WaveObject.from_wave_file(audio)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def msgToBinary(msg):
  if type(msg)== str:
    return ''.join([format(ord(i),"08b") for i in msg])
  elif type(msg) == int or type(msg)== np.uint8:
    return format(msg,"08b") 
  elif type(msg) == bytes or type(msg) == np.ndarray:
    return [format(i,"08b") for i in msg]
  else:
    return "Invalid Input type !!"

def writeAttachment(length):
    with open("attachment.txt", "r+") as fw:
        data = "This file is an acknowledgement for the requested audio file. We hope you are happy with our response !!"+"\ncopyright @ IIT Bhubaneswar_"+str(length)
        te = fw.read()
        fw.seek(0)
        fw.write(re.sub(r"<string>ABC</string>(\s+)<string>(.*)</string>", r"<xyz>ABC</xyz>\1<xyz>\2</xyz>", data))
        fw.truncate()

    fw.close

def encode(message):
    audio = wave.open("coverAudio.wav", mode='rb')
    data = bytearray(list(audio.readframes(audio.getnframes())))
    #print(len(data))
    bits=msgToBinary(message)
    length=len(bits)
    print("Message length : ",length)
    writeAttachment(length)
    np.random.seed(len(bits))
    perm = np.random.permutation(len(bits))
    j=0 
    #do a mask and or with the message bit
    for bit in bits:
        data[perm[j]] = (int(data[perm[j]]) & 254) | int(bit)
        j+=1

    dataModified = bytes(data)

    with wave.open('embedded.wav', 'wb') as fd:
        fd.setparams(audio.getparams())
        fd.writeframes(dataModified)
    audio.close()

    print("\nMessage is embedded into embedded.wav file")

def decode():
    f = open("attachment.txt", "r")
    lines = f.read().splitlines()
    last_line = lines[-1]
    length = last_line.split("_")[-1]
    #print(length)
    seed =int(length)
    np.random.seed(seed)
    perm = np.random.permutation(seed)
    audioNew = wave.open("embedded.wav", mode='rb')
    newData = bytearray(list(audioNew.readframes(audioNew.getnframes())))
    extractedData = [newData[i] & 1 for i in perm]
    decodedMessage = "".join(chr(int("".join(map(str,extractedData[i:i+8])),2))
                                         for i in range(0,len(extractedData),8))
    print("Hidden Message :",decodedMessage)

if __name__== "__main__":
    while(1):
        print("\nChoose appropriate option: \n1.Encode\n2.Decode\n3.Play Embedded Audio\n4.Play Original audio\n5.exit")
        val = int(input("\nChoice:"))
        if val == 1:
            msg = input("\nEnter the secret message : ")
            encode(msg)
        elif val == 2:
            decode()
        elif val == 3:
            print("\nPlaying embedded.wav audio...")
            playAudio("embedded.wav")
            print("\n Done !!")
        elif val == 4:
            print("\nPlaying coverAudio.wav audio...")
            playAudio("coverAudio.wav")
            print("\n Done !!")
        elif val == 5:
            print("\nExitting...")
            quit()
        else :
            print("\nInvalid choice !!")


