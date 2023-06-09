FROM python:3.9.1
EXPOSE 5000
RUN mkdir app
ADD ./requirements.txt /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install Flask
RUN pip install --upgrade --no-cache-dir git+https://github.com/StreamAlpha/tvdatafeed.git
ADD ./* .
ENTRYPOINT ["python"]
CMD ["app.py"]
