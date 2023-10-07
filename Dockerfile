FROM python

WORKDIR requirements.txt /app/

COPY requirements.txt /app/

RUN pip install -r requirements.txt


