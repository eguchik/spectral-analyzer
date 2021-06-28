FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y sudo

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN sudo sed -i.org -e 's|ports.ubuntu.com|jp.archive.ubuntu.com|g' /etc/apt/sources.list
RUN sudo apt-get update

RUN sudo apt-get install -y build-essential libbz2-dev libdb-dev \
  libreadline-dev libffi-dev libgdbm-dev liblzma-dev \
  libncursesw5-dev libsqlite3-dev libssl-dev \
  zlib1g-dev uuid-dev

RUN sudo apt-get install -y python3
RUN sudo apt-get install -y python3-pip
RUN python3 -m pip install django numpy pandas django-cleanup scipy pyper plotly

RUN sudo apt-get install -y software-properties-common
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
RUN sudo apt-get update
RUN sudo apt-get install -y r-base
RUN R -e "install.packages('ica')"


