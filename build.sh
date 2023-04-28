#usr/bin/sh
pip install -r requirement.txt
pip install --upgrade --no-cache-dir git+https://github.com/StreamAlpha/tvdatafeed.git
gunicorn app:app