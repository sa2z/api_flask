#!/bin/bash

apt-get update

INSTALL_PKGS="git zip nano wget curl build-essential ca-certificates gnupg lsb_release unixodbc unixodbc-dev tesseract-ocr tesseract-ocr-kor"
for i in $INSTALL_PKGS; do
  sudo apt-get install -y $i
done

git clone https://github.com/sa2z/api_flask.api /code
pip3 install -r /code/api_flask/requirements.txt
