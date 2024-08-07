import os, sys
try:
    __import__("kunci_txt").main()
except Exception as e:
    exit(str(e))