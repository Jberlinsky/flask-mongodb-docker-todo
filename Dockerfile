FROM python:3.6.6-slim-jessie

RUN apt-get update && apt-get install -y --no-install-recommends \
		git \
	&& rm -rf /var/lib/apt/lists/*


ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD app /app/

EXPOSE 8000

WORKDIR /app/app/

CMD gunicorn -b 0.0.0.0:8000 wsgi:app
