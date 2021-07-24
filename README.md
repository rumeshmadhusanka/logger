# logger
Log to a file via a REST endpoint

Install:
```
pip install uvicorn fastapi
```

Start:
```
uvicorn logger:app --port 8000 --host 0.0.0.0
```

Fetch logs:
```
curl http:localhost:8000
```

Send logs:
``` 
curl --header "Content-Type: application/json" \ 
                   --request POST \<br>
                   --data '{"text":"hello worl log"}' \ 
                   http://localhost:8000 
 ```


Create a system service:<br>
Place the logger.service file in `/etc/systemd/system/` directory
```
systemctl start logger.service
```
