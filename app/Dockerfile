FROM python:3.12.2-alpine3.19
WORKDIR /app
COPY . .
RUN apk add --no-cache bash postgresql-libs 
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev 
RUN pip install -r requirements.txt 
ENV FLASK_APP=app.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]