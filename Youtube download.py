# -*- coding: utf-8 -*-
"""
Spyder Editor
Effettua il download del video dalla sito di youtube
This is a temporary script file.
"""

from __future__ import unicode_literals
import youtube_dl
import urllib3
import shutil

ydl_var={ }
with youtube_dl.YoutubeDL(ydl_var) as ydl:
    ydl.download(["https://www.youtube.com/watch?v=AtVPsPct4KM"])
