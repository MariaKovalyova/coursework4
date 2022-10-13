from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссёры', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Сталоне'),
})

movie: Model = api.model('Фильмы', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Фильм1'),
    'description': fields.String(required=True, max_length=256, example='Пример описания'),
    'trailer': fields.String(required=True, max_length=100, example='https://www.youtube.com/watch?v=zweB54NntQA'),
    'year': fields.Integer(required=True, example=1999),
    'rating': fields.Float(required=True, example=7.8),
    'genre': fields.Nested(genre),
    'director_id': fields.Nested(director)
})

user: Model = api.model('Пользователи', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='user@gmai.com'),
    'password': fields.String(required=True, max_length=100, example='123456'),
    'name': fields.String(required=True, max_length=100, example='Vladimir'),
    'surname': fields.String(requried=True, max_length=100, example='Yakin'),
    'genre': fields.Nested(genre)
})


