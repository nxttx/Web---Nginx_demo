# Nginx demo
Het doel van deze demo is om een nginx server op te zetten met een loadbalancer en een reverse proxy. De loadbalancer zal de requests verdelen over de twee verschillende web servers. De gehele omgeving zal in een docker container draaien.

## Uiteindelijke architectuur
```plantuml
@startuml
node "Docker network" as container {
    node "Nginx" as nginx
    component "Express" as web1
    component "Flask" as web2
    ' files 
    file "index.html" as index
}
node "Host" as host {
    node "Browser" as browser
}

browser -down-> nginx : (80, http) send request to and get response from
nginx -down-> web1 : (80, http) redirect request to
nginx -down-> web2 : (80, http) redirect request to
nginx -down-> index : (80, http) serve static file

@enduml
```

## Losse onderdelen uitvoeren:
```bash
$ cd Express # or cd Flask
$ docker build -t webserver . && docker run -p 80:80 webserver # build and run the docker container
```