# logger
Log to a file via a REST endpoint

Install:

`$ pip install uvicorn fastapi`

Start:

`$ uvicorn logger:app --port 8000 --host 0.0.0.0`


Create a system service:

Place the logger.service file in /etc/systemd/system directory

`$ systemctl start logger.service`
