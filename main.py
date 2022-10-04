from attr import has
from matplotlib.animation import MovieWriter
from moviepy.editor import *
import json 
from attr import has
from PIL import Image
import requests
from io import BytesIO

import random
import string



script = json.load(open("scripts/script1.json"))
final_scene = []
cache = []


def scenebuilder(background, duration, text, textColor, textStroke, textSize, font, gif_theme):
    background = ImageClip(getImage(background)).set_duration(duration)
    gif = VideoFileClip("assets/gifs/"+gif_theme+".gif").loop(10).set_duration(duration)
    txt_clip = TextClip(text,fontsize=textSize,color=textColor, stroke_color=textStroke, stroke_width=2, font=font)
    txt_clip = txt_clip.set_pos('center').set_duration(duration)
    video = CompositeVideoClip([background, gif, txt_clip])
    return video


def getImage(theme):
    filename = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    cache.append(filename)
    resource = urllib.urlopen("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "/cache/"+ filename +".jpg")
    output = open("/cache/" + filename + ".jpg","wb")
    output.write(resource.read())
    output.close()
    return "/cache/"+ filename +".jpg"

for i in script['scenes']:
    final_scene.append(scenebuilder(i['background_theme'], i['duration'], i['text'], i['textColor'], i['textStroke'], i['textSize'], i['textFont'], i['gif_theme']))


video = CompositeVideoClip(final_scene)
video.write_videofile("edited.mp4", fps=25, threads=4)


