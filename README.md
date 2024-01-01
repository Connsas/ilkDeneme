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
#Proje için docker ayarlamaları.
FROM python:3.11.3

WORKDIR /opt/odev1/ilkDeneme

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /opt/odev1/ilkDeneme/requirements.txt
RUN pip install -r requirements.txt

COPY . /opt/odev1/ilkDeneme/
```
