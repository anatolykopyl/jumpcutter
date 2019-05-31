from pytube import YouTube
import os
import subprocess

testfiles = ["30fps.mp4", "60fps.mp4", "15fps.mp4"]


def downloadFile(url):
    sep = os.path.sep
    originalPath = YouTube(url).streams.first().download()
    filepath = originalPath.split(sep)
    filepath[-1] = filepath[-1].replace(' ', '_')
    filepath = sep.join(filepath)
    os.rename(originalPath, filepath)
    return filepath


def downloadTestdata():
    p = downloadFile("https://www.youtube.com/watch?v=aqz-KE-bpKQ")
    command = ["ffmpeg", "-i", p, "-r", "15", "-t", "00:01:00", "15fps.mp4"]
    subprocess.run(command)
    command = ["ffmpeg", "-i", p, "-r", "60", "-t", "00:01:00", "60fps.mp4"]
    subprocess.run(command)
    command = ["ffmpeg", "-i", p, "-t", "00:01:00", "30fps.mp4"]
    subprocess.run(command)


# prepare testdata if missing
for src in testfiles:
    if(not os.path.isfile(src)):
        downloadTestdata()

print("15fps autodetection test")
command = ["python3", "jumpcutter.py", "--input_file",
           "15fps.mp4", "--output_file", "t.mp4"]
subprocess.run(command)
assert(os.path.getsize("t.mp4") == 8443196)
