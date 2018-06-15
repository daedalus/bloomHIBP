# Bloom HIBP – check Have i been Pwnd with bloom filters in pure python



Installing:

    git clone https://github.com/daedalus/fastBloomFilter

    or
   
    sudo pip install fastbloomfilter

Geting the HIBP file (https://downloads.pwnedpasswords.com/passwords/pwned-passwords-ordered-2.0.txt.7z.torrent):

    7z e -so -bd pwned-passwords-ordered-2.0.txt.7z | cut -c 1-40 > 40.txt
  
Using:

    python3 loadbloom.py 40.txt HIBP_128MB.blf

    python3 checkbloom HIBP_128MB.blf "blah"
