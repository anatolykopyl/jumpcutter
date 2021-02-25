from pytube import YouTube
import os
import subprocess

testfiles = ["30fps.mp4", "60 fps.mp4",
             "15fps.mp4", "soundless.mp4", "music.mp4"]


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
    command = ["ffmpeg", "-i", p, "-r", "15", "-t", "00:01:00", testfiles[2]]
    subprocess.run(command)
    command = ["ffmpeg", "-i", p, "-r", "60", "-t", "00:01:00", testfiles[1]]
    subprocess.run(command)
    command = ["ffmpeg", "-i", p, "-t", "00:01:00", testfiles[0]]
    subprocess.run(command)
    command = ["ffmpeg", "-i", testfiles[0], "-an", testfiles[3]]
    subprocess.run(command)
    command = ["ffmpeg", "-i", testfiles[0], "-vn", testfiles[4]]
    subprocess.run(command)
    os.remove(p)


# prepare testdata if missing
for src in testfiles:
    if(not os.path.isfile(src)):
        print("missing "+src)
        downloadTestdata()

print("15fps autodetection test")
command = ["python3", "jumpcutter.py", "--input_file",
           testfiles[2], "--output_file", "t.mp4"]
subprocess.run(command)
assert(os.path.getsize("t.mp4") == 8443196)
os.remove("t.mp4")

print("30fps autodetection test")
command = ["python3", "jumpcutter.py", "--input_file",
           testfiles[0], "--output_file", "t.mp4"]
subprocess.run(command)
assert(os.path.getsize("t.mp4") == 8571040)
os.remove("t.mp4")

print("60fps autodetection test + space test")
command = ["python3", "jumpcutter.py", "--input_file",
           testfiles[1], "--output_file", "t t.mp4"]
subprocess.run(command)
assert(os.path.getsize("t t.mp4") == 8113359)
os.remove("t t.mp4")

print("soundless test")
command = ["python3", "jumpcutter.py", "--input_file",
           testfiles[3], "--output_file", "t.mp4"]
subprocess.run(command)

print("music test")
command = ["python3", "jumpcutter.py", "--input_file",
           testfiles[4], "--output_file", "t.mp4"]
subprocess.run(command)

print("audio_only music test")
command = ["python3", "jumpcutter.py", "--input_file",
           testfiles[4], "--output_file", "t.mp4", "--audio_only"]
subprocess.run(command)
assert(os.path.getsize("t.mp4") == 565547)
os.remove("t.mp4")

print("audio_only video test")
command = ["python3", "jumpcutter.py", "--input_file",
           testfiles[2], "--output_file", "t.mp4", "--audio_only"]
subprocess.run(command)
assert(os.path.getsize("t.mp4") == 408510)

print("slowdown test + force test")
command = ["python3", "jumpcutter.py", "--input_file",
           testfiles[2], "--output_file", "t.mp4", "--force", "--sounded_speed", "0.5", "--silent_speed", "0.9"]
subprocess.run(command)
assert(os.path.getsize("t.mp4") == 22962113)
os.remove("t.mp4")

print("low quality test")
command = ["python3", "jumpcutter.py", "--input_file",
           testfiles[2], "--output_file", "t.mp4", "--frame_quality", "31", "--crf", "50", "--preset", "ultrafast"]
subprocess.run(command)
assert(os.path.getsize("t.mp4") == 796732)
os.remove("t.mp4")

print("phasevocoder test")
command = ["python3", "jumpcutter.py", "--input_file",
           testfiles[2], "--output_file", "t.mp4", "--stretch_algorithm", "phasevocoder", "--sounded_speed", "0.5"]
subprocess.run(command)
assert(os.path.getsize("t.mp4") == 19991295)
os.remove("t.mp4")

print("edl test")
command = ["python3", "jumpcutter.py", "--input_file",
           testfiles[2], "--output_file", "t.edl", "--edl"]
subprocess.run(command)
assert(os.path.getsize("t.edl") == 1464)
os.remove("t.edl")