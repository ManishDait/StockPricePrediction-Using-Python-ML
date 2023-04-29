FROM python:3.8-alpine
EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip install -r requirement.txt
RUN pip install Flask
RUN pip install --upgrade --no-cache-dir git+https://github.com/StreamAlpha/tvdatafeed.git
ENTRYPOINT ["python"]
CMD ["app.py"]
