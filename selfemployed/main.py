import sys
from scrapy import cmdline
import os, subprocess, time


def exec_proc(name):
    if name:
        cmdline.execute(name.split())


if __name__ == '__main__':
    print('[*] beginning main thread')
    if os.path.isfile('output.json'):
        os.remove('output.json')
    name = "scrapy crawl selfemployed -o output.json --logfile logfile.txt"
    exec_proc(name)
    print('[*] main thread exited')
    print('main stop====================================================')



