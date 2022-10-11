FROM python:3.9.14-slim-buster
WORKDIR /app
COPY ./src/* .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"] 