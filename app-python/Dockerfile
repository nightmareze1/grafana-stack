FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY src/requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src /app

WORKDIR /app

CMD [ "python", "main.py" ]

EXPOSE 3001
