Система Управления Инвентаризацией Продукции

Система управления инвентаризацией продукции - позволяет пользователям эффективно управлять информацией о продуктах и предприятиях, включая добавление, обновление, удаление и просмотр деталей.

Основные Функции

- **CRUD операции**: Поддержка создания, чтения, обновления и удаления информации о продуктах и предприятиях.
- **Пагинация**: Эффективный просмотр списков продуктов и предприятий благодаря встроенной поддержке пагинации.
- **Docker-контейнеризация**: Легкая настройка и развертывание приложения благодаря использованию Docker.
- **Swagger документация**: Автоматически сгенерированная документация API для удобства использования и тестирования.

Технологии

- Django и Django REST Framework для разработки бэкенда.
- PostgreSQL для хранения данных.
- Docker для контейнеризации и упрощения развертывания.
- Swagger для документации API.

Начало Работы

Чтобы запустить проект локально, вам понадобится Docker и Docker Compose.

Шаги для запуска:

1. Клонируйте репозиторий:

```bash
git clone <ссылка на ваш репозиторий>
cd <имя вашего проекта>

2. Запустите приложение с помощью Docker Compose:
docker-compose up --build

После запуска приложение будет доступно по адресу http://localhost:8000/.

Использование API
После запуска приложения вы можете взаимодействовать с API через Swagger UI по адресу http://localhost:8000/swagger/. Это предоставит вам интерактивный интерфейс для тестирования всех доступных эндпоинтов API.

Тестирование
Для запуска тестов используйте следующую команду:

docker-compose run web python manage.py test
