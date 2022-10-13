from project.config import config
from project.server import create_app
from project.setup.db import db

if __name__ == '__main__':  # Создаст таблицы для БД
    with create_app(config).app_context():
        db.drop_all()
        db.create_all()

"""
Создание таблиц. После создания таблиц зпустить файл заполнения базы даннх "load_fixtures.py" из основного каталога
"""