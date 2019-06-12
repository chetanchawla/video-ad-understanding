from pytube import YouTube
##pytube is a library used to fetch an scrape data off youtube
yt = YouTube('https://www.youtube.com/watch?v=q31tGyBJhRY')
#this creates a youtube type object which takes a parameter of the video's viewable link
print("Title is ",yt.title)
print("Description \n",yt.description)
print("Rating ",yt.rating)
print("Video Length (sec) ",yt.length)
print("Views",yt.views)
print("Streams \n ",yt.streams.all())
stream=yt.streams.filter(file_extension='mp4').all()
stream[0].download()