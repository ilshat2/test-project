### Задание A1: "Собери и запусти" (Docker, Linux, CLI)
1. Директория `test-project` создана.

2. Dockerfile создан:
```
test-project/Dockerfile
```

3. Сборка образа:

![](images/create_image.png)

4. Запуск контейнера:

![](images/docker_run.png)

5. Cтраница в браузере:

![](images/localhost.png)

6. docker-compose.yml файл:
```
test-project/docker-compose.yml
```

7. Чтобы доставить index.html в контейнер без пересборки образа, можно использовать docker volumes. Как это прописано в docker-compose.yml:
```
    volumes:
      - ./index.html:/usr/share/nginx/html/index.html
```

### Задание B1: "Простой скрипт-помощник" (Bash)
...

### Задание B2: "Маленькая проблема в Git" (Git)

![](images/task_b2.png)


