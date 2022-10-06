from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
import json 
import numpy as np




script = json.load(open("scripts/script1.json"))
final_scene = []
cache = []
current_time = 0
screensize = (1920,1080)



def scenebuilder(background, duration, text, textColor, textStroke, textSize, font, gif_theme):
    global current_time
    global screensize
    backgroundi = ImageClip(background).set_duration(duration).resize(screensize)
    gif = VideoFileClip("assets/gifs/gif3.gif", has_mask=True)
    gif = gif.set_fps(7)
    gif = gif.loop(True)
    gif = gif.set_duration(duration)
    txt_clip = TextClip(text,fontsize=textSize,color=textColor, stroke_color=textStroke, stroke_width=2, font=font).set_duration(10)
   
    video = CompositeVideoClip([backgroundi, gif, txt_clip.set_pos('center')], size=screensize)
    current_time = current_time + duration




    return video




for i in script['scenes']:
    final_scene.append(scenebuilder(i['background_theme'], i['duration'], i['text'], i['textColor'], i['textStroke'], i['textSize'], i['textFont'], i['gif_theme']))


video = concatenate_videoclips(final_scene)
video.write_videofile("edited.mp4", fps=25)




