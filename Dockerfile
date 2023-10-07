FROM python

WORKDIR /app/

COPY requirements.txt /app/

COPY db.json /app/

COPY entrypoint.sh /app/

COPY requirements.txt /app/

RUN pip install -r requirements.txt
