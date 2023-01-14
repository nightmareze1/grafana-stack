# Launch Monitoring Stack: 
```
docker-compose up --build
```

## Demo:

Run from terminal:

```
curl localhost -H"Host: app1.com" -I -XGET
curl localhost/eze -H"Host: app1.com" -I -XGET
while : ; do curl localhost -H"Host: app1.com" -I -XGET && curl localhost/eze -H"Host: app1.com" -I -XGET; done

```

Open the URL and explore (click these links):

http://localhost:3000/d/A0DfKMcik/traefik-status-codes-microservices?orgId=1&refresh=5s&var-service=app1-grafana-stack@docker&var-interval=1m&var-simple_query=container

http://localhost:3000/explore


# Dashboards:

traefik: http://localhost:8080/

grafana: http://localhost:3000/

prometheus: http://localhost:9090/

loki: http://localhost:3100/

app1: http://app1.com

zipkin: http://localhost:9411/zipkin/?lookback=15m&endTs=1673705203034&limit=10

prometheus: http://localhost:9090


# Grafana read prometheus data and dashboard with status codes , response time ,etc.

Grafana: http://localhost:3000 #Login with admin #user: admin #pass: test

# For test metrics
traefik: http://localhost:8080/metrics

View metrics in prometheus using dashboard and querys.

prometheus: http://localhost:9090


# Stop Stack:
```
docker-compose down
```
