FROM python:3.11.4

WORKDIR /website

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["waitress-serve", "--port=5000", "application:app"]