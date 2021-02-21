The idea behind LSB embedding is that if we change the last bit value of a
pixel, there won’t be much visible change in the color.This approach has the
advantage that it is the simplest one to understand, easy to implement and results in
stego-images that contain embedded data as hidden.

The disadvantage of Least Significant Bit is that it is vulnerable to steganalysis
and is not secure at all. So as to make it more secure, the least significant bit
algorithm is modified to work in a different way. This proposed approach simply does
not pick up least significant bits of pixel in a sequence but it intelligently selects pixel
positions for embedding the secret message.


Execution commands :

python ImageSteg.py

After compilation it displays the following 

choose an operation :
1.Encode/Encryption
2.Decode/Decryption
3.Compute PSNR

If you choose operation 1 : (Encoding)

        choose a cover image :
        1. cover1.png
        2. cover2.png

        After choosing cover image it asks for secret message. Input the secret or hidden message.
        Then it asks for a name to save the encoded/embedded image into project directory. Provide an input name with png extension.

        And encoding is done :)
        Same can be done for cover image 2 also.

If you choose operation 2 : (Decoding)

It asks you to provide the corresponding encoded cover image. provide the name of encoded image that you have saved earlier.

And then it displays decoded hidden message.

If you choose operation 3 : compute PSNR

It asks you to provide original and steganographed image names with png extension.
Once they are provided psnr score will be displayed.