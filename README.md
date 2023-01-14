# You need add in your /etc/host


127.0.0.1 app1.com

# Later, running: 

docker-compose up --build

# Check works urls:

prometheus: http://localhost:9090/

loki: http://localhost:3100/

# Dashboaords

traefik: http://localhost:8080/

grafana: http://localhost:3000/

app1: http://app1.com

zipkin: http://localhost:9411/zipkin/?lookback=15m&endTs=1673705203034&limit=10

prometheus: http://localhost:9090



## Demo:

Open url:

http://localhost:3000/d/A0DfKMcik/traefik-status-codes-microservices?orgId=1&refresh=5s&var-service=app1-grafana-stack@docker&var-interval=1m&var-simple_query=container

http://localhost:3000/explore?orgId=1&left=%7B%22datasource%22:%22KAmJXlhVz%22,%22queries%22:%5B%7B%22refId%22:%22A%22,%22datasource%22:%7B%22type%22:%22loki%22,%22uid%22:%22KAmJXlhVz%22%7D,%22editorMode%22:%22builder%22,%22expr%22:%22%7Bcontainer%3D%5C%22app1%5C%22%7D%20%7C%3D%20%60%60%22,%22queryType%22:%22range%22%7D%5D,%22range%22:%7B%22from%22:%22now-1h%22,%22to%22:%22now%22%7D%7D

Run with terminal:
```
curl localhost -H"Host: app1.com" -I -XGET
curl localhost/eze -H"Host: app1.com" -I -XGET

while : ; do curl localhost -H"Host: app1.com" -I -XGET && curl localhost/eze -H"Host: app1.com" -I -XGET; done

```

# Grafana read prometheus data and dashboard with status codes , response time ,etc.

Grafana: http://localhost:3000 #Login with admin #user: admin #pass: test

# For test metrics

traefik: http://localhost:8080/metrics

or

View metrics in prometheus using dashboard and querys.

# Stop Stack:

docker-compose down
