FROM python:3.9.1
EXPOSE 5000
COPY ./requirements.txt /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirement.txt
RUN pip install Flask
RUN pip install --upgrade --no-cache-dir git+https://github.com/StreamAlpha/tvdatafeed.git
COPY ./* .
ENTRYPOINT ["python"]
CMD ["app.py"]
