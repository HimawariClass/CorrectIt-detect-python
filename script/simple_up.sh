#!/bin/bash
docker build -t crctit-detect .
docker run -it --rm -v $(pwd):/app crctit-detect /bin/bash