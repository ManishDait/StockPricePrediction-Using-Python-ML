FROM python:3.8-alpine
EXPOSE 5000
COPY . /app
WORKDIR /app
RUN ./build.sh
ENTRYPOINT ["python"]
CMD ["app.py"]
