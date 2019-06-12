FROM ubuntu

RUN apt-get update

RUN apt-get install -y \
    python3-minimal \
    python3-pip \
    ffmpeg \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip

EXPOSE 5000

WORKDIR /jumpcutter/
COPY . ./

RUN pip3 install -r requirements.txt
