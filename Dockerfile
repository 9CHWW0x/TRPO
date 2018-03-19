FROM ubuntu:14.04

MAINTAINER carlad "https://github.com/9CHWW0x"

# Install packages for building ruby
RUN apt-get update
RUN apt-get install -y --force-yes git python3
RUN apt-get clean

RUN git clone https://github.com/9CHWW0x/TRPO /root/TRPO
