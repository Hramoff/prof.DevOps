FROM python:3.9-alpine
WORKDIR /FS
COPY . /FS/

RUN pip install -r requirements.txt

CMD python3.9 /finitastory/manage.py runserver