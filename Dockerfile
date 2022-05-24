FROM ubuntu:18.04
LABEL Description="Build environment"

ENV HOME=/root

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get -y --no-install-recommends install \
    build-essential \
    gcc \
    gdb \
    wget

RUN apt-get install -y libedit-dev 
RUN apt-get install -y libeditline-dev 
RUN apt-get install -y zlib1g 
RUN apt-get install -y m4 
RUN apt-get install -y git 
RUN apt-get install -y zlib1g-dev

WORKDIR /opt/async


RUN git clone https://github.com/asyncvlsi/act.git

WORKDIR /opt/async/act

ENV ACT_HOME=/opt/async
ENV VLSI_TOOLS_SRC=/opt/async/act



RUN ./configure ${ACT_HOME}
RUN ./build

RUN make install
RUN make runtest
RUN echo "${PATH}:${ACT_HOME}/bin:"
ENV PATH="${PATH}:${ACT_HOME}/bin:"

RUN apt-get install python3
RUN git clone https://github.com/GenRincewind/ACT-Online-Sandbox.git