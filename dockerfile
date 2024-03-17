FROM python:3.10-bookworm

RUN apt-get update && \
    apt-get install -y \
    build-essential

WORKDIR /usr/src/app

COPY . .

RUN pip3 install --upgrade pip && \
    pip3 install .

RUN python3 post_install.py

CMD ["sh"]