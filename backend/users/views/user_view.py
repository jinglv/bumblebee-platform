import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View

from backend.exception.custom_exception import CustomException, ErrorCode
from backend.utils.api_response import response_success
from backend.utils.log import default_log
from users.forms import UserForm


class UsersView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        """
        代表登录
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = UserForm(request.GET)
        result = form.is_valid()
        if not result:
            default_log.error(form.errors.as_json())
            raise CustomException()

        user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if user:
            # 登录持久化， 生成session
            login(request, user)
            return response_success("登录成功")
        else:
            raise CustomException(ErrorCode.USER_LOGIN_FAIL)

    @staticmethod
    def post(request, *args, **kwargs):
        """
        代表的是注册
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 返回的是字符串
        body = request.body
        # 把字符串进行解析为字典
        data = json.loads(body)

        form = UserForm(data)
        result = form.is_valid()
        if not result:
            default_log.error(form.errors.as_json())
            raise CustomException()

        if User.objects.filter(username=form.cleaned_data["username"]).exists():
            raise CustomException(ErrorCode.USER_EXIST)

        user = User.objects.create_user(username=form.cleaned_data["username"],
                                        password=form.cleaned_data["password"])
        if user:
            login(request, user)  # 登录持久化， 生成session
            return response_success("注册成功")
        else:
            raise CustomException(ErrorCode.REGISTER_FAIL)

    @staticmethod
    def delete(request, *args, **kwargs):
        """
        代表的是注销
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        logout(request)
        return response_success("注销成功")
