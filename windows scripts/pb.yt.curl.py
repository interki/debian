#!/usr/bin/env python
import json, urllib.request, datetime, subprocess
from sys import executable
from subprocess import *
import pickle
# from colorama import *
# from colorama import Fore

# init()

# init(autoreset=True)

class colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   ITALIC = '\e[3m'
   END = '\033[0m'

## Default player 
player = "mpv"

back_str = "'b' = Back  'q' = Quit"
s_range = 10 

def column(self):
    widths = [max(map(len, col)) for col in zip(*self)]
    for row in self:
        print ("  ".join((val.ljust(width) for val, width in zip(row, widths))))

    # back_str = "'b' = Back  'q' = Quit"
    ## user input select broadcast
    # print ('\n',back_str.rjust(50))
    # option = (input("broadcast #no.? "))
def selector():
    if option == ("B") or option == ("b"):
        select_user()
    if channel == ("Q") or channel == ("q"):
        exit()

def manual_select():
    global channel
    print ('\n',"'b' = Back  'q' = Quit".rjust(50))
    channel = input("Enter Channel? ")
    if channel == ("B") or channel == ("b"):
        select_user()
    if channel == ("Q") or channel == ("q"):
        exit()
    try:
        twitch()
    except urllib.error.HTTPError:
        print ("\n"+colour.YELLOW+"*Doesn't Exist*"+colour.END)
        manual_select()
        
def search_range():
    global s_range
    s_range = int(input("change scan range "))
    select_user() 

def player_select():
    global player 
    print ('\n',"'m' = mpv   'b' = bakaMplayer  'h' = mpc-HC\n")   
    ps_option = input("selection? ")

    if ps_option == ("M") or ps_option == ("m"):
        player = "mpv"
    if ps_option == ("B") or ps_option == ("b"):
        player = "baka"
    if ps_option == ("H") or ps_option == ("h"):
        player = "mpc-HC"

    select_user()

def ping_test():

    run = str("ping -n 1 8.8.8.8")
    handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
    link = (str(handle.stdout.read()))
    # print (type(str(handle.stdout.read())))
    # print (colour.DARKCYAN+ link2 +colour.END)
    # print (run)
    handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
    print (handle.stdout.read())
    
    select_user()
    # exit()

def twitch_url():
    option = input('insert twitch vod url: ')
    print("")
    
    video_id = option[29:] 
    url = (f'https://api.twitch.tv/kraken/videos/{video_id}/?client_id=jzkbprff40iqj646a697cyrvl0zt2m6')
    # print (url,'\n')
    info = json.loads(urllib.request.urlopen(url, timeout = 15).read().decode('utf-8'))
    print (colour.CYAN+ info['title'] +colour.END, '\n')
    resolution = (info['fps'])

    k = 0
    for key in resolution:
        k = k + 1
        print('{}:'.format(k), key)

    qual = (input('\nquality #no.? // Press Enter for defualt (source)\n'))
    if qual == "":
        qual = "best"
    else:
        qual = list(resolution)[int(qual) - 1]
    if qual == "chunked":
        qual = "best"

    run = str(f"streamlink {option} {qual} --player-passthrough=hls --stream-url")
    handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
    link = (str(handle.stdout.read()))
    link2 = (link[2:-5])
    print (colour.DARKCYAN+ link2 +colour.END)
    run = str(f"start mpv.exe {link2} --demuxer-thread=yes and --demuxer-readahead-secs=5000 --no-terminal")
    handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)

    select_user()

def select_user():
        global platform, channel
        ## select twitch/yt user
        # print ("1: sips_\n2: pyrionflax\n3: hatfilms extra\n4: yogslive\n")
        puser = [
                ["1:", "sips_"],
                ["2:", "pyrionflax"],
                ["3:", "hatfilms extra"],
                ["4:", "yogslive"],
                ["5:", "hutch"],
                ["6:", "sacriel"],
                ["7:", "anderZEL"],
                ["8:", "Notser"],
                ["9:", "Syanoks"],
                ["10:", "NinjaTrappeur"],
                ["11:", "Team Double Dragon"],
                ["12:", "tsoding"],
                ["13:", "shroud"]
                ]

        print("")
        column(puser)

        # try:
        #     oldblist = pickle.load( open( "pbyt.p", "rb") )
        #     last_yt_title = oldblist[1][1]
        #     print (last_yt_title)
        # except NameError:
        #     print ("blist not found?")
        # except FileNotFoundError:
        #     print ("pickle not found") 
        

        string = f"'{colour.YELLOW}m{colour.END}' = Manual Entry    '{colour.YELLOW}p{colour.END}' = Select Player    '{colour.YELLOW}s{colour.END}' = Scan Range    '{colour.YELLOW}q{colour.END}' = Quit\n"
        # string = "'"+colour.YELLOW+"m"+colour.END+"'"+" = Manual Entry  '"+colour.YELLOW+"q"+colour.END+"'"+" = Quit"
        print ('\n', string.rjust(68))
        # print ('\n',"'m' = Manual Entry  'q' = Quit".rjust(50))
        # print ('\n1: {}\n2: {}\n3: {}\n4: {}\n5: {}\n6: {}\n7: {}\n8: {}\n9: {}\n10: {}\n'.format('sips_', 'pyrionflax', 'hatfilms extra', 'yogslive', 'hutch', 'sacriel', 'anderZEL', 'Notser', 'Syanoks', 'NinjaTrappeur'))
        # print (back_str.rjust(50))
        channel = input(colour.YELLOW+"channel #no.? "+colour.END)

        if channel == ("B") or channel == ("b"):
            select_user()
        if channel == ("Q") or channel == ("q"):
            exit()
        if channel == ("M") or channel == ("m"):
            manual_select()
        if channel == ("S") or channel == ("s"):
            search_range()
        if channel == ("P") or channel == ("p"):
            player_select()
        if channel == ("T") or channel == ("t"):
            ping_test()
        if channel == ("U") or channel == ("u"):
            twitch_url()
        if channel == ("Y") or channel == ("y"):
            ustream()

        ## convert user input into channel string
        channel = {
            "1":    "sips_",
            "2":    "pyrionflax",
            "3":    "UCJYvnogbZIQQvX9exn5aDPw",
            "4":    "UCQBs359lwzyVFtc22LzLjuw",
            "5":    "hutch",
            "6":    "sacriel",
            "7":    "anderzel",
            "8":    "notser",
            "9":    "syanoks",
           "10":    "ninjatrappeur",
           "11":    "UCZ3edpZNi_qmuBG2FIHW5tQ",
           "12":    "tsoding",
           "13":    "shroud"
           }.get(channel, "food")

        if 'UC' in channel:
            platform = 'yt'
            you_tube(channel)
        else:
            platform = 'twitch'
            twitch()

def you_tube(channel):
    global platform, blist, option
    print ('\n{}YouTube{}\n'.format(colour.RED, colour.END))
    ## JSON
    res_yt = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/activities?part=snippet,contentDetails&channelId={0}&key=AIzaSyCTm4oQFPZTxEkNKmY1C4KfLwmPHz9t880&maxResults=50'.format(channel))
    res_body_yt = res_yt.read()
    j_yt = json.loads(res_body_yt.decode("utf-8"))

    blist = []
    
    if (j_yt['items'][0]['snippet']['title']) == (j_yt['items'][1]['snippet']['title']):
        # print ('doubles')
        doubles = True
    else:
        # print ('no doubles')
        doubles = False
    
    # iterations = 20 if doubles == True else 10
    itera = s_range *2 if doubles == True else s_range

    try:
        oldblist = pickle.load( open( channel, "rb") )
        pickle_found = True
        # print (oldblist)
        # last_yt_title = oldblist[1][1]
    except NameError:
        print ("blist not found?")
        pickle_found = False
    except FileNotFoundError:
        print ("pickle not found") 
        pickle_found = False

    last_yt_title = oldblist[1][1] if pickle_found == True else "no last yt title"
    # print (last_yt_title)
    
    if last_yt_title == (j_yt['items'][0]['snippet']['title']) and s_range == 10:
        print (colour.CYAN+"-"+colour.END)
        match_old = True
    

    # try:
    #     last_yt_title
    # except NameError:
    #     var_exists = False
    # else:
    #     var_exists = True
    #
    # print(var_exists)
    #
    else:
        match_old = False
        if doubles == True:
            for x in range (itera):
                if (x % 2 == 0):
                    title = (j_yt['items'][x]['snippet']['title'])
                    try:
                        idd = (j_yt['items'][x]['contentDetails']['upload']['videoId'])
                    except KeyError:
                        print ('key error msg')

                    created_at = (j_yt['items'][x]['snippet']['publishedAt'])

                    dt_obj = datetime.datetime.strptime(created_at,'%Y-%m-%dT%H:%M:%S.%fZ')
                    tdelta = datetime.timedelta(hours=10)
                    dt = dt_obj + tdelta
                    adate = (str(dt)[5:10])
                    atime = (str(dt)[11:16])

                    res2 = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/videos?id={0}&part=contentDetails&key=AIzaSyCTm4oQFPZTxEkNKmY1C4KfLwmPHz9t880'.format(idd))
                    res_body2 = res2.read()
                    j2 = json.loads(res_body2.decode("utf-8"))

                    length = (j2['items'][0]['contentDetails']['duration'])
                    
                    y = (int(x / 2))
                    # y = x

                    alist = [str(y+1), title, length[2:], adate, atime]
                    # alist = [str(y+1), title, length[2:], created_at[5:10], created_at[11:16]]
                    # print (alist)
                    blist.append(alist)

        elif doubles == False:
            for x in range (itera):
                # if (x % 2 == 0):
                    title = (j_yt['items'][x]['snippet']['title'])
                    try:
                        idd = (j_yt['items'][x]['contentDetails']['upload']['videoId'])
                    except KeyError:
                        print ('key error msg')

                    created_at = (j_yt['items'][x]['snippet']['publishedAt'])

                    dt_obj = datetime.datetime.strptime(created_at,'%Y-%m-%dT%H:%M:%S.%fZ')
                    tdelta = datetime.timedelta(hours=10)
                    dt = dt_obj + tdelta
                    adate = (str(dt)[5:10])
                    atime = (str(dt)[11:16])

                    res2 = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/videos?id={0}&part=contentDetails&key=AIzaSyCTm4oQFPZTxEkNKmY1C4KfLwmPHz9t880'.format(idd))
                    res_body2 = res2.read()
                    j2 = json.loads(res_body2.decode("utf-8"))

                    length = (j2['items'][0]['contentDetails']['duration'])
                    
                    # y = (int(x / 2))
                    y = x

                    alist = [str(y+1), title, length[2:], adate, atime]
                    # alist = [str(y+1), title, length[2:], created_at[5:10], created_at[11:16]]
                    # print (alist)
                    blist.append(alist)

        cblock = [colour.RED, "", "", "", ""]
        headings = ["#:", "Title:", "Length:", "Date:", "Time:"]
        cblock_end = [colour.END, "", "", "", ""]
        # blist.insert(0, cblock)
        blist.insert(0, headings)
        # blist.insert(2, cblock_end)

        # pickle.dump( blist, open( "pbyt.p", "wb") )
        pickle.dump( blist, open( channel, "wb") )

        # widths = [max(map(len, col)) for col in zip(*blist)]
        # for row in blist:
        #     print ("  ".join((val.ljust(width) for val, width in zip(row, widths))))    
        # print("")

    # id_old = {channel: blist}
    # print (id_old)

    column(oldblist) if match_old == True else column(blist)

            # space = " " if len(length) >= 9 else "" 

    print ("\n",back_str.rjust(50))
    option = (input("video #no.? "))
    selector()
    # if option == ("B") or option == ("b"):
    #     select_user()
    # if channel == ("Q") or channel == ("q"):
    #         exit()
    
    if doubles == True: 
        vidno = (int(option) - 1) * 2
    else:
        vidno = (int(option) - 1) 

    id2 = (j_yt['items'][vidno]['contentDetails']['upload']['videoId'])
    url = ('https://www.youtube.com/watch?v={0}'.format(id2))

    print ('playing: {0}'.format(colour.DARKCYAN+(j_yt['items'][vidno]['snippet']['title'])+colour.END))

    ## Send to windows clipboard for automatic play with SVPtube
    # subprocess.run(['clip.exe'], input=url.strip().encode('utf-16'), check=True)

    run = str("youtube-dl -f 22 -g {}".format(url))
    handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
    link = (str(handle.stdout.read()))
    link2 = (link[2:-3])
    print ("\n{}".format(link2))
    
    if player == "mpv":
        # run = str("start mpv.exe \"{}\" --demuxer-thread=yes and --demuxer-readahead-secs=1000 --no-terminal".format(link2))
        run = str("start /B mpv --ytdl-format=bestvideo+bestaudio {} --no-terminal".format(url))
    if player == "mpc-HC":
        run = str("\"C:\Program Files\MPC-HC\mpc-hc64.exe\" \"{}\"".format(link2))
    if player == "baka":
        run = ("\"C:\\Users\\i5b\\Desktop\\BakaMplayer\\Baka MPlayer.exe\" \"{}\"".format(url))

    # print (run)
    handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)

    select_user()
    # exit()
    
def twitch():
    ## jason request twitch api
    res = urllib.request.urlopen('https://api.twitch.tv/kraken/channels/{}/videos?broadcasts=true&client_id=caozjg12y6hjop39wx996mxn585yqyk'.format(channel))
    res_body = res.read()
    j = json.loads(res_body.decode("utf-8"))

    # check if channel currently live
    url = 'https://api.twitch.tv/kraken/streams/' + channel +"/?client_id=jzkbprff40iqj646a697cyrvl0zt2m6"
    info = json.loads(urllib.request.urlopen(url, timeout = 15).read().decode('utf-8'))
    if info['stream'] == None:
        print ("\n{}Twitch{}".format(colour.PURPLE, colour.END))
    else:
        print ("\n{}Twitch{} - {}*LIVE*{}".format(colour.PURPLE, colour.END, colour.GREEN, colour.END))

    print ('')

    ## check if total videos is <=9 
    total = (j['_total'])
    # if total <= 9:
    #     itera = total
    # else:
    #     itera = 10

    itera = total if total <= 9 else 10

    blist = []

    ## iterate through past broadcasts collecting information for display
    for x in range (itera):
        title = (j['videos'][x]['title'])
        length = (j['videos'][x]['length'])
        created_at = (j['videos'][x]['created_at'])
        game = (j['videos'][x]['game'])
        url = (j['videos'][x]['url'])
    
        ano = str(x+1)
        alength = str(datetime.timedelta(seconds=(length)))
        
        dt_obj = datetime.datetime.strptime(created_at,'%Y-%m-%dT%H:%M:%SZ')
        tdelta = datetime.timedelta(hours=10)
        dt = dt_obj + tdelta
        bdate = (str(dt)[5:10])
        btime = (str(dt)[11:16])

        alist = [ano, title, alength, bdate, btime, game]
        blist.append(alist)

    ## format and print broadcast information
    headings = ["#:", "Title:", "Length:", "Date:", "Time:", "Game:"]
    blist.insert(0, headings)
    widths = [max(map(len, col)) for col in zip(*blist)]
    for row in blist:
        print ("  ".join((val.ljust(width) for val, width in zip(row, widths))))

    ## user input select broadcast
    print ('\n',back_str.rjust(50))
    option = (input("broadcast #no.? "))

    if option == ("B") or option == ("b"):
        select_user()
    if channel == ("Q") or channel == ("q"):
            exit()

        # platform = ""
        # break
    ## convert user input into base 0, and collect relevant video url
    vidno = (int(option) - 1)
    opt = (j['videos'][vidno]['url'])

    resolution = ((j['videos'][vidno]['resolutions']))

    # del resolution['chunked']
    keys = set(resolution.keys())
    # print(resolution)

    print('\n')
    ## reset qual
    # qual = "empty"
    k = 0
    for key in resolution:
        k = k + 1
        print('{}:'.format(k), key)

    if 'p' or 'chunked' in str(keys): 
        qual = (input('\nquality #no.? // Press Enter for defualt (source)\n'))
        # qual = (input('\nquality #no.? '))
        # print('\n')
        # print (type(qual))

        # if qual == "" or "chunked":
        if qual == "":
            qual = "best"
        else:
            qual = list(resolution)[int(qual) - 1]
        if qual == "chunked":
            qual = "best"

    else:
        qual = input('\nquality #no.? // Press Enter for defualt (high)\n')
        qual = {
            '1':    list(resolution)[0],
            '2':    list(resolution)[1],
            '3':    list(resolution)[2],
            '4':    list(resolution)[3],
            # '5':    list(resolution)[4],
            # '6':    list(resolution)[5],
            }.get(qual, 'high')
    print ("\n"+qual, "Selected..")

    print ("\nstarting....\n")

    ## pass request to streamlink in external shell
    # run = str("streamlink {0} {1} --player-passthrough=hls".format(opt, qual))
    # handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
    # print (handle.stdout.read())

    ## pass to mpv and detatch 
    run = str("streamlink {0} {1} --player-passthrough=hls --stream-url".format(opt, qual))
    # run = str("streamlink https://www.twitch.tv/videos/141016850?t=3h23m40s 720p30 --player-passthrough=hls --stream-url")
    handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
    link = (str(handle.stdout.read()))
    # print (type(str(handle.stdout.read())))
    link2 = (link[2:-5])
    print (colour.DARKCYAN+ link2 +colour.END)

    if player == "mpv": 
        # run = str("start mpv.exe {} --demuxer-thread=yes and --demuxer-readahead-secs=10000 cache=1000000 --no-terminal".format(link2))
        # run = str("start mpv.exe {} --demuxer-thread=yes and --demuxer-readahead-secs=5000 --no-terminal".format(link2))
        run = str("start mpv.exe {} --no-terminal".format(link2))
    if player == "mpc-HC":
        run = str("\"C:\Program Files\MPC-HC\mpc-hc64.exe\" {}".format(link2))
    if player == "baka":
        run = str("\"C:\\Users\\i5b\\Desktop\\BakaMplayer\\Baka MPlayer.exe\" {}".format(link2))

    # print (run)
    handle = Popen((run), stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
    # print (handle.stdout.read())
    
    select_user()
    # exit()

def ustream():
    ## jason request twitch api
    # res = urllib.request.urlopen('https://api.ustream.tv/channels/509347/videos.json')
    # res_body = res.read()
    # j = json.loads(res_body.decode("utf-8"))
    #
    # check if channel currently live
    url = 'https://api.ustream.tv/channels/509347/videos.json'
    info = json.loads(urllib.request.urlopen(url, timeout = 15).read().decode('utf-8'))
    # if info['stream'] == None:
    #     print ("\n{}Twitch{}".format(colour.PURPLE, colour.END))
    # else:
    #     print ("\n{}Twitch{} - {}*LIVE*{}".format(colour.PURPLE, colour.END, colour.GREEN, colour.END))

    print ('')
    for x in range (10):
        print (info['videos'][x]['title'])

    select_user()

select_user()
