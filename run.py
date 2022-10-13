from project.config import config
from project.models import Genre, Director, User, Movie
from project.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():  # Импорт дополнительный объектов ключ/значение
    return {
        "db": db,
        "Genre": Genre,
        "User": User,
        "Movie": Movie,
        "Director": Director
    }


if __name__ == '__main__':  # Запуск сервера
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )
"""http://localhost:8080/ """