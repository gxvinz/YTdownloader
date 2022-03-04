#YOUTUBE_VIDEO_DOWNLOAD

from pytube import YouTube

link = input("Enter the link: ")
vid = YouTube(link)

#printing information on video
print("Title: ", vid.title)
print("Views: ", vid.views)
print("Length: ", vid.length, "seconds")
print("Rating: ", vid.rating)

print(vid.streams)
print(vid.streams.filter(only_audio=True))
print(vid.streams.filter(progressive=True))
copy = vid.streams.get_highest_resolution()
copy.download()