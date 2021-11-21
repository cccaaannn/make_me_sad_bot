FROM ubuntu

# install system dependencies
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

# copy app
COPY . /make_me_sad

# install python dependencies
WORKDIR /make_me_sad
RUN pip3 install -r requirements.txt

# run
WORKDIR /make_me_sad/src
CMD ["python3", "run.py"]
