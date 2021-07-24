# logger
Log to a file via a REST endpoint

Install:<br>
`$ pip install uvicorn fastapi`

Start:<br>
`$ uvicorn logger:app --port 8000 --host 0.0.0.0`


Create a system service:<br>
Place the logger.service file in /etc/systemd/system directory<br>
`$ systemctl start logger.service`
