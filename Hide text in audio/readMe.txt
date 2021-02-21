The idea behind LSB embedding is that if we change the last bit value of an
audio sample, there won’t be much change in quality of the audio.This approach has
the advantage that it is the simplest one to understand, easy to implement and
results in stego-audio file that contains the embedded data as hidden.

The disadvantage of Least Significant Bit is that it is vulnerable to steganalysis
and is not secure at all. So as to make it more secure, the least significant bit
algorithm is modified to work in a different way. This proposed approach follows
hiding any form of digital data into uncompressed digital audio files in a random
manner. It uses two intermediates to convey the secret data. An uncompressed audio
file acting as a carrier file holding the secret data inside the LSBs of its audio samples
and an attachment.txt file which will be used while recovering a secret message.

Algorithm is provided in report.pdf

Execution commands :

python AudioSteg.py

After compilation it displays the following 

choose an operation :
1.Encode/Encryption
2.Decode/Decryption
3.play Audio
4.exit

If you choose operation 1 : (Encoding)
			Enter the secret or hidden message.
			Then the audio file with embedded secret message will be created with name 'embedded.wav'
			Also an attachment.txt file will be created which will be used in decoding.

If you choose operation 2 : (Decoding)
			Your hidden message will be displayed.


If you choose operation 3 : embedded Audio file will be played. 
