FROM python:latest

WORKDIR /usr/app/src

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY laba5.py ./
COPY laba5Test.py ./

CMD ["pytest", "laba5Test.py"]
