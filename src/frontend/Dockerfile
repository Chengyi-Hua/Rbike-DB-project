FROM nickgryg/alpine-pandas:3.8

ENV FLASK_APP app.py
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . .

RUN apk update && apk add gcc \
    libc-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    g++ \
    postgresql-dev 
RUN pip install -r requirements.txt

EXPOSE 4800

CMD ["python", "frontend.py"]