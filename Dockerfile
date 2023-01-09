FROM python:3.10.6-alpine

WORKDIR /app

RUN apk add chromium-chromedriver

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]