# epub-shrink
shrink epub file size by reducing image quality

# Idea

I only read epub files when converted to mobi on my Kindle, so those huge epubs with high quality pictures mean little to me.

This script decompress .epub files and reduce quality of all .jpg files within.


#Prerequisits

You need Pillow to run it (since PIL is unavailable to Python 3, as far as I know).

* I thought about using pingo.exe to compress .jpgs, but settled with Pillow in the end. Let me know if you have suggestions concerning other approaches.

