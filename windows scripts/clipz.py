import time
import sys
import os
# sys.path.append(os.path.abspath("SO_site-packages"))

from subprocess import *

import pyperclip

recent_value = ""
while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        # print ("Value changed: %s" % str(recent_value)[:20])
        print (recent_value)
        if "watch?v=" in recent_value:
            print("YouTube Match")
            # mpv --ytdl-format=bestvideo+bestaudio $YOUTUBE_VIDEO_URL
            # run = str("start /B mpv \"--ytdl-format=bestvideo+bestaudio\" {} --no-terminal --osd-level=0".format(recent_value))
            # run = str("start /B mpv \"--ytdl-format=bestvideo[height<=1920]+bestaudio/best[height<=1920]\" {} --no-terminal --osd-level=0".format(recent_value))
            if "&" in recent_value:
                sep = ("&")
                # trimmed_value = sep.join(recent_value.split(sep)[:-1])
                trimmed_value = sep.join(recent_value.split(sep)[:1])
                print (trimmed_value)
                run = str("start /B mpv \"--ytdl-format=bestvideo[height<=1920]+bestaudio/best[height<=1920]\" {} --no-terminal --osd-level=0 --cache=99999 ".format(trimmed_value))
                handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
            else:
                run = str("start /B mpv \"--ytdl-format=bestvideo[height<=1920]+bestaudio/best[height<=1920]\" {} --no-terminal --osd-level=0 --cache=99999 ".format(recent_value))
                handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
            # link = (str(handle.stdout.read()))
            # print(link)
        if "www.ustream.tv/recorded/" in recent_value:
            print("Ustream Match")
            # run = str("streamlink {} best --player-passthrough=hls --stream-url".format(recent_value))
            run = str("streamlink {} best --stream-url".format(recent_value))
            handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
            link = (str(handle.stdout.read()))
            link2 = (link[2:-5])
            run = str("start /B mpv \"{}\" --no-terminal".format(link2))
            handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
        if "https://vimeo.com/" in recent_value:
            print("Vimeo Match")
            run = str("youtube-dl -f http-1080p -g {} --no-warnings".format(recent_value))
            handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
            link = (str(handle.stdout.read()))
            link2 = (link[2:-3])
            run = str("start /B mpv \"{}\" --no-terminal".format(link2))
            handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
        if "https://www.twitch.tv/videos/" in recent_value:
            print("Twitch VOD Match")
            # run = str("streamlink {} best --player-passthrough=hls --stream-url".format(recent_value))
            run = str("streamlink {} best --stream-url".format(recent_value))
            handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
            link = (str(handle.stdout.read()))
            link2 = (link[2:-5])
            run = str("start /B mpv \"{}\" --no-terminal --osd-level=0".format(link2))
            # run = str("start /B mpv \"{}\" --demuxer-thread=yes and --demuxer-readahead-secs=5000 --no-terminal --osd-level=0".format(link2))
            handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
        elif "https://www.twitch.tv/" in recent_value:
            print("Twitch Channel Match")
            # run = str("streamlink {} best --player-passthrough=hls --stream-url".format(recent_value))
            run = str("streamlink {} best --stream-url".format(recent_value))
            handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
            link = (str(handle.stdout.read()))
            link2 = (link[2:-5])
            run = str("start /B mpv \"{}\" --no-terminal".format(link2))
            handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)


    time.sleep(1.0) 
