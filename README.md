# youtube_api

docker image :- 
https://hub.docker.com/repository/docker/regostar/rego_youtube

To run :-
docker-compose up

kill->
docker-compose down

makemigrations ->
docker-compose run web python manage.py makemigrations

migrate->
docker-compose run web python manage.py migrate

----------------------

Navigate to http://localhost:8000/home/

search and view pagenated results.

By default it is pagenated sorted by published datetime.


![dashboard](https://github.com/regostar/youtube_api/blob/main/img/1.png)


![dashboard](https://github.com/regostar/youtube_api/blob/main/img/2.png)


![search](https://github.com/regostar/youtube_api/blob/main/img/3.png)
