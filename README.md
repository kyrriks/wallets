# wallets app

### Требования
- docker
- docker compose

## Как запустить проект

### Сборка и запуск контейнеров

1. `docker-compose build`
2. `docker compose up -d`
3. Зайти в контейнер web и применить миграции 

```python
python wallets/manage.py migrate
```


## Как запустить тесты

1. **Зайти в контейнер с django приложением**
2. **Перейти в директорию проекта**

```
cd wallets
```

3. **Запустить тесты**

```
pytest
```


## API Endpoints
Приложение предоставляет следующие API эндпоинты:

- **GET /wallets/{wallet_uuid}**: Получение информации о кошельке.
- **POST /wallets/{wallet_uuid}/operation**: Выполнение транзакции на кошельке.

# Документация API
Документация API доступна по адресу: **http://localhost:8000/swagger/