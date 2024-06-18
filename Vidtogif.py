from moviepy.editor import VideoFileClip

clip=VideoFileClip("bunny.mp4")
clip.write_gif("bunny1.gif")