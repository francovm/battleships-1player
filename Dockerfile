FROM python:3
# Maintainer info
LABEL maintainer="Franco Vega Mercado"

WORKDIR /app

COPY . .

RUN python /app/setup.py develop

#CMD ["python", "./src/main.py"]
