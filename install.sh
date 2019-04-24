#!/bin/bash

sudo apt-get update
sudo apt-get install python3.6
sudo apt install python3-pip
sudo pip3 install virtualenv
sudo apt-get install whois

virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python threatRipper.py
deactivate
clear