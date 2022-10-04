# Import everything needed to edit video clips





background = ImageClip("assets/images/photo.jpg").set_duration(10)
gif = VideoFileClip("assets/gifs/gif2.gif").loop(10).set_duration(10)
gif.set_position(40, 40)
gif = gif.set_position(lambda t: ('center', 50+t) )
txt_clip = TextClip("Ich wünsche dir einen \nschönen Start in den Montag!",fontsize=70,color='blue', stroke_color='red', stroke_width=2, font='Pacifico-Regular')

txt_clip = txt_clip.set_pos('center').set_duration(10)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([background, gif, txt_clip])

# Write the result to a file (many options available !)
video.write_videofile("myHolidays_edited.mp4", fps=25, threads=4)




