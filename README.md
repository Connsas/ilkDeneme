# ilkDeneme Projesi
Github'a alışmak için ilk çatallanması önerilen deneme proje.

Aşşağıdaki yapıda daha önceden oluşturduğumuz api bir servise dönüştürülüyor ve gunicorn ile 5 workerla çalıştırılıyor, böylece herhangi bir workerın çökmesi durumunda bütün sistem çökmüyor.
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

Nginx için ayarlamalar.
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

