import os
from time import sleep
import webbrowser



filename = input()
links = []
try:
    with open(os.path.dirname(os.path.realpath(__file__))+"/"+filename, "r") as r:
        links = [line.rstrip() for line in r]
except Exception as e:
    print(e)
    exit(1)

for item in links:
    t = webbrowser.open(item)
    sleep(3)