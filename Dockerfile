FROM       python:3.7-alpine
WORKDIR    /app
COPY       requirements.txt ./requirements.txt
RUN        pip install -r requirements.txt
COPY       ./*.py ./ 
CMD        [ "python", "./threatRipper.py" ]