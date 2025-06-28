FROM alpine:3.22.0

WORKDIR /src

RUN apk update && apk upgrade \
&& apk add --no-cache python3 py3-pip \
&& apk add --no-cache python3-tkinter tcl tk \
&& apk add --no-cache openssl ffmpeg

RUN python3 -m venv venv
ENV PATH="venv/bin:$PATH"

RUN python3 -m pip install --upgrade pip setuptools wheel
RUN pip install customtkinter gtts pydub requests pillow

COPY *.png /src/
COPY *.py /src/
