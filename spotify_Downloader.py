from spotify_dl import spotify_dl



# url = input("Enter Spotify l")
url = input("Enter Spotify Link (Song/ PlayList / Album) : ")
direc = "./"

spotify_dl.spotify_dl(url,direc)

