#!/bin/bash

sudo apt-get update
sudo apt-get install python3.7
sudo apt install python3-pip
sudo pip3 install virtualenv
sudo apt-get install whois

cd ..
virtualenv venv
source venv/bin/activate
cd threatRipper/
pip3 install -r requirements.txt
python3 threatRipper.py