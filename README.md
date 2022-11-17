## Start project with Docker


1. Git clone
```
https://github.com/Vital28/sender.git
```
2. Open project in IDE

3. Add TOKEN in  .evn file: ```TOKEN = '<your token>'```
4. Start Docker 
``` 
docker compose up --build
 ```

5. Add migrations:
``` 
docker compose exec web python manage.py makemigrations sending
docker compose exec web python manage.py migrate
 ```
 
6. Docker stopped 
```
docker compose stop
docker compose down
```
***
```http://0.0.0.0:8000/api/``` 

```http://0.0.0.0:8000/api/clients/``` 

```http://0.0.0.0:8000/api/sending/``` 

```http://0.0.0.0:8000/api/mailings/fullinfo/``` - all sending statistic

```http://0.0.0.0:8000/api/mailings/<pk>/info/``` - personal sending statistic

```http://0.0.0.0:8000/api/messages/``` 

```http://0.0.0.0:8000/docs/``` - swagger 

```http://0.0.0.0:5555``` - celery flower

***



