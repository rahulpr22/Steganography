import cv2
import numpy as np
import math

def msgToBinary(msg):
  if type(msg)== str:
    return ''.join([format(ord(i),"08b") for i in msg])
  elif type(msg) == int or type(msg)== np.uint8:
    return format(msg,"08b") 
  elif type(msg) == bytes or type(msg) == np.ndarray:
    return [format(i,"08b") for i in msg]
  else:
    return "Invalid Input type !!"

def lsb(img,data):
    max_bytes = img.shape[0] * img.shape[1] * 3 // 8

    if len(msgToBinary(data)) > max_bytes:
        raise ValueError("Error encountered insufficient bytes, need bigger img or less data !!")

 

    secretkey= msgToBinary( 0b11010010)
    binData=msgToBinary(data)
    counter=0
    for values in img:
        for pixel in values:
            r, g, b = msgToBinary(pixel)
            if counter< len(binData) and (int(r[-2]) ^ int(secretkey[2]) == 1):
                pixel[0] = int(r[:-1] + binData[counter], 2)
                counter += 1
            if counter< len(binData) and int(g[-2]) ^ int(secretkey[1]) == 1:
                pixel[1] = int(g[:-1] + binData[counter], 2)
                counter += 1
            if counter< len(binData) and int(b[-2]) ^ int(secretkey[1]) == 1:
                pixel[2] = int(b[:-1] + binData[counter], 2)
                counter += 1
            if counter >= len(binData):
                break
    return img

def PSNR(original, stego): 
    mse = np.mean((original - stego) ** 2) 
    if(mse == 0):  
        return 100
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse)) 
    return psnr

def helperEncoder(srcimg):
  data=input("\nInput secret message that you want to hide : ")
  if (len(data) == 0): 
        raise ValueError('Data is empty..!!')
  LSB=lsb(srcimg,data+str("$"))
  iName=input("\nInput a name for the steganographed/encoded image with extension :\n")
  cv2.imwrite(iName,LSB)
  print("\nSaving the steganographed image.....\nImage saved with the name "+str(iName)+"\n")


def encode():
  print("\nChoose by which image you want to test...\n")
  print("\n1. cover1.png\n2. cover2.png")
  choice = int(input())
  if choice==1:
    srcimg=cv2.imread('cover1.png')
    helperEncoder(srcimg)
  elif choice==2:
    srcimg=cv2.imread('cover2.png')
    helperEncoder(srcimg)
  else :
    print("\Invalid choice\nExitting...\n")
    

def decode():
  secretkey= msgToBinary( 0b11010010)
  img=cv2.imread(input("\nInput corresponding steganographed image with extension to extract your secret message : "))
  binarydata=""
  for values in img:
        for pixel in values:
            r, g, b = msgToBinary(pixel)
            if  (int(r[-2]) ^ int(secretkey[2]) == 1):
              binarydata +=  r[-1]
            if  (int(g[-2]) ^ int(secretkey[1]) == 1):
              binarydata +=  g[-1]
            if  (int(b[-2]) ^ int(secretkey[1]) == 1):
              binarydata +=  b[-1]
  split_by_8_bytes = [ binarydata[i: i+8] for i in range(0, len(binarydata), 8) ]
  decoded_data = ""
  for byte in split_by_8_bytes:
      decoded_data += chr(int(byte, 2))
      if decoded_data[-1:] == "$": 
          break

  return decoded_data[:-1]

def ComputePSNR():
  original = cv2.imread(input("Input original cover Image with extension : "))
  stego = cv2.imread(input("Input corresponding Steganographed Image with extension : "))
  print("PSNR Score --> ",PSNR(original,stego))

def run():
  print("\nChoose appropriate option..\n")
  print("1.Encode\n2.Decode\n3.Compute PSNR Score\n")
  choice = int(input())
  if choice==1:
    encode()
  elif choice==2:
    print("\n Your secret message is :\n",decode())
    print("\n")
  elif choice==3:
    ComputePSNR()
  else:
    print("Invalid choice !!")


if __name__== "__main__":
    run()
    choice= input("Do you wish to continue? y/n : ")
    while choice=='y':
        run()
        choice= input("\n\nDo you wish to continue? y/n : ")
        if choice=='n':
          break

    print("\n")
