FROM r-base

COPY requirements.txt ./
RUN apt update

RUN apt-get install -y build-essential libbz2-dev libdb-dev \
  libreadline-dev libffi-dev libgdbm-dev liblzma-dev \
  libncursesw5-dev libsqlite3-dev libssl-dev \
  zlib1g-dev uuid-dev tk-dev

RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN python3 -m pip install -r requirements.txt
RUN R -e "install.packages('ica')"