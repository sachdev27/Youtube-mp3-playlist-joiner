import youtube_dl
import re 


# -------------------------------------------------------

url = input("Youtube Url : ")




ydl_opts = {
    'format': 'bestaudio/best',
    # 'outtmpl':  url.replace("https://","") + '/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
} 



with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      info_dict = ydl.extract_info(url, download=False)
    #   video_url = info_dict.get("url", None)
    #   video_id = info_dict.get("id", None)
      video_title = info_dict.get('title', None)
      title = "".join(re.findall("[a-zA-Z]+", video_title))
      ydl_opts["outtmpl"] =  title  + '/%(title)s.%(ext)s'



with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])