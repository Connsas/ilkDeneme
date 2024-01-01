# ilkDeneme Projesi
Github'a alışmak için ilk çatallanması önerilen deneme proje.

```
//Aşşağıdaki yapıda daha önceden oluşturduğumuz api bir servise dönüştürülüyor ve gunicorn ile 5 workerla çalıştırılıyor, böylece herhangi bir workerın çökmesi durumunda bütün sistem çökmüyor.
[Unit]
Description=AKYG dersi icin olsuturdugum api in servise cevirilmesi.
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/opt/odev1/ilkDeneme
ExecStart=/usr/bin/gunicorn --workers 5 --bind unix:merhaba.sock -m 007 wsgi:app //Burada herhangi bir porta bağlamak yerine sokete bağlıyoruz.

[Install]
WantedBy=multi-user.target
```
```
//Nginx için ayarlamalar.
server {
listen 6767; //Port forwardingte vm de 6767 portunu kullandığım için burada 6767 portunu giriyorum.

location / {
  include proxy_params;
  proxy_pass http://unix:/opt/odev1/ilkDeneme/merhaba.sock;
 }


location /static  {
    include  /etc/nginx/mime.types;
    root /opt/odev1/ilkDeneme/;
  }
}
```
```python
from merhaba import app

if __name__ == "__main__":
    app.run
```
```
#birden fazla containerın birbiriyle haberleşmesini sağladığınız conf dosyası.
version: '3.8'

services:
  web:
    build: /opt/odev1/ilkDeneme
    command: gunicorn --workers 5 --bind 0.0.0.0:5001 merhaba:app //container çalıştırıldığı zaman gunicorn ile ayağa kaldırıyoruz.
    ports:
      -  5000:5001 
  nginx:
    build: /opt/odev1/ilkDeneme/nginx
    command: sudo systemctl start nginx.service 
    ports:
      - 81:80
    depends_on:
      - web
```
```
#Proje için docker ayarlamaları.
# pull official base image
FROM python:3.11.3

# set work directory
WORKDIR /opt/odev1/ilkDeneme

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /opt/odev1/ilkDeneme/requirements.txt // indirmemiz gereken bağımlılıkları txt den okuyarak containera dahil ediyor.
RUN pip install -r requirements.txt

# copy project
COPY . /opt/odev1/ilkDeneme/
```
```
#requirements.txt'nin içi projede gerekli bağımlılıkların belirtildiği yer.
flask
pandas
requests
flask_restful
gunicorn
```
```
#projede kullandığım nginx için ayarlamalar.
upstream hello_flask {
    server web:5000;
}

server {

    listen 80;

    location / {
        proxy_pass http://web:5000;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }

}
```
```
#nginx conatineri için dockerfile.
FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
```
