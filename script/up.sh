#! /bin/bash
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\" &
open -a xquartz
docker run -it --rm -e DISPLAY=$(ifconfig en0 | awk '$1 == "inet" {print $2}'):0 -v $(pwd):/app namedpython/python-opencv-with-gui /bin/bash
