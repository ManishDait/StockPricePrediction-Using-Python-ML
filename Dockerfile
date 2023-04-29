FROM python:3.8-alpine
EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip3 install -r requirement.txt
RUN pip3 install Flask
RUN pip3 install --upgrade --no-cache-dir git+https://github.com/StreamAlpha/tvdatafeed.git
ENTRYPOINT ["python"]
CMD ["app.py"]
