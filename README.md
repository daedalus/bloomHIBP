![lint_python](https://github.com/daedalus/bloomHIBP/workflows/lint_python/badge.svg)
[![GitHub issues](https://img.shields.io/github/issues/daedalus/bloomHIBP.svg)](https://github.com/daedalus/bloomHIBP/issues)
[![GitHub forks](https://img.shields.io/github/forks/daedalus/bloomHIBP.svg)](https://github.com/daedalus/bloomHIBP/network)
[![GitHub stars](https://img.shields.io/github/stars/daedalus/bloomHIBP.svg)](https://github.com/daedalus/bloomHIBP/stargazers)

# Bloom HIBP – check Have i been Pwnd with bloom filters in pure python

Idea taken from https://www.bloomingpassword.fun/

### Installing dependencies: ###

```
git clone https://github.com/daedalus/fastBloomFilter
cd fastbloomfilter
sudo pip install -e .
```

or

```
sudo pip install fastbloomfilter
```

### Grab the HIBP file (https://downloads.pwnedpasswords.com/passwords/pwned-passwords-ordered-2.0.txt.7z.torrent): ###

```
7z e -so -bd pwned-passwords-ordered-2.0.txt.7z | cut -c 1-40 > 40.txt
```
  
### Using it: ###

```
python3 loadbloom.py 512MB 40.txt HIBP_512MB.blf
python3 checkbloom HIBP_512MB.blf "blah"
```
