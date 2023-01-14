# You need add in your /etc/host


127.0.0.1 app1.com

# Later, running: 

docker-compose up --build

# Check works urls:
prometheus: http://localhost:9090/
loki: http://localhost:3100/

# Traefik dashboaord

traefik: http://localhost:8080/

grafana: http://localhost:3000/

app1: http://app1.com


Test:

Open url: http://localhost:3000/d/A0DfKMcik/traefik-status-codes-microservices?orgId=1&refresh=5s

Run with terminal:
```
curl localhost -H"Host: app1.com" -I -XGET
curl localhost/eze -H"Host: app1.com" -I -XGET

while : ; do localhost -H"Host: app1.com" -I -XGET ; done
```

# Grafana read prometheus data and dashboard with status codes , response time ,etc.

Grafana: http://localhost:3000 #Login with admin #user: admin #pass: test

# For test metrics

traefik: http://localhost:8080/metrics

or

View metrics in prometheus using dashboard and querys.

# Stop Stack:

docker-compose down
