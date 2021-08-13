from pydub import AudioSegment
import os

def two(a):
    if len(str(a))==1:
        return '0'+str(a)
    else:
        return str(a)

def convertTime(ms):
    ms/=1000
    hr = int(ms/60/60)
    minn = int((ms-hr*60*60)/60)
    sec = int((ms-(minn*60)-(hr*60*60)))
    s = ''
    if hr!=0:
        s=f"{hr}:{two(minn)}:{two(sec)}"
    else:
        s=f"{two(minn)}:{two(sec)}"
    return s

# path = "./Playlist1"

path = input("Enter PlayList Path (Relative / Absolute) : ")



dir_list = os.listdir(path) 


file = open ("TimeStamp.txt",'w') 


# # print the list 
# print(dir_list) 

file.write( f"00:00 {dir_list[1].replace('.mp3','')}\n"  )
full_song = AudioSegment.from_mp3(path + "/" + dir_list[0])
# full_song = AudioSegment.from_mp3( "./" + dir_list[0])
print(0,dir_list[0])

for i,v in enumerate(dir_list[2:]):
    print(i+1,v)
    song_path = path + "/" + v
    sound = AudioSegment.from_mp3(song_path)
    file.write( f"{convertTime(len(full_song))} {v.replace('.mp3','')}\n"  )
    full_song += sound

song = input('Enter Mix Song Name : ')

full_song.export(song, format='mp3',bitrate='312k')

print("Song has been saved in the Current Directory as : "+ song +".mp3")