import mplayer
import commands

temp=commands.getoutput("mplayer /home/pi/Desktop/test.mp4 -vf dsize=320:-2 -geometry 0:0")
print temp