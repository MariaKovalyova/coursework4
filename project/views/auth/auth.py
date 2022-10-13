from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user

api = Namespace('auth')

"""Добавление (регистрация) нового пользователя в базу данных"""
@api.route('/register/')
class RegisterView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def post(self):
        data = request.get_json(force=True)
        if data.get('email') and data.get('password'):
            return user_service.create_user(data.get('email'), data.get('password')), 201
        else:
            return "Ошибка 401", 401

"""Авторизация пользователя"""
@api.route('/login/')
class LoginView(Resource):
    """Авторизация пользователя"""
    @api.response(404, 'Not Found')
    def post(self):
        data = request.get_json(force=True)
        if data.get('email') and data.get('password'):
            return user_service.check(data.get('email'), data.get('password')), 201
        else:
            return "Ошибка 401", 401

    """ОБновление токена"""
    @api.response(404, 'Not Found')
    def put(self):
        data = request.get_json(force=True)
        if data.get('access_token') and data.get('refresh_token'):
            return user_service.update_token(data.get('refresh_token')), 201
        else:
            return "Ошибка 401", 401

