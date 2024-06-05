FROM python:3.11.4

WORKDIR /website

COPY . .

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["waitress-serve", "--listen=0.0.0.0:8080", "application:app"]