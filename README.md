# jumpcutter
Automatically edits videos. Explanation here: https://www.youtube.com/watch?v=DQ8orIurGxw

## Some heads-up:

It uses Python 3.

It works on Ubuntu 16.04 and Windows 10. (It might work on other OSs too, we just haven't tested it yet.)

This program relies heavily on ffmpeg. It will start subprocesses that call ffmpeg, so be aware of that!

As the program runs, it saves every frame of the video as an image file in a
temporary folder. If your video is long, this could take a LOT of space.
I have processed 17-minute videos completely fine, but be wary if you're gonna go longer.

I want to use pyinstaller to turn this into an executable, so non-techy people
can use it EVEN IF they don't have Python and all those libraries. Jabrils 
recommended this to me. However, my pyinstaller build did not work. :( HELP

## Building with nix
`nix-build` to get a script with all the libraries and ffmpeg, `nix-build -A bundle` to get a single binary.

## Building without nix
### Windows
Something along the lines of
1. Download https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe
2. Execute downloaded File -> Click Install Python
3. Download https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20190612-caabe1b-win64-static.zip
4. Extract downloaded File
5. Download https://github.com/lamaun/jumpcutter/archive/master.zip
6. Extract downloaded File
7. Move ffmpeg/bin/ffmpeg.exe to jumpcutter-master/jumpcutter-master folder
8. Open cmd
9. cd C:\Users\YOUR_USERNAME_HERE\Downloads\jumpcutter-master\jumpcutter-master
10. C:\Users\YOUR_USERNAME_HERE\AppData\Local\Programs\Python\Python37\python.exe -m pip install -r requirements.txt
11. C:\Users\YOUR_USERNAME_HERE\AppData\Local\Programs\Python\Python37\python.exe jumpcutter.py --input_file input.mp4

### Linux
```BASH
sudo apt-get install python3-minimal python3-pip ffmpeg
cd /some/folder/you/like/
# For https:
git clone https://github.com/Lamaun/jumpcutter.git
# For ssh:
git clone git@github.com:Lamaun/jumpcutter.git
cd jumpcutter
pip3 install -r requirements.txt # you might want --user
```

### Docker
```
docker build -t jumpcutter .
docker exec -it jumpcutter
```

## Usage
```BASH
python3 jumpcutter.py --help # get an overview of the available commands
python3 jumpcutter.py --input_file some_input_video.mp4
```
