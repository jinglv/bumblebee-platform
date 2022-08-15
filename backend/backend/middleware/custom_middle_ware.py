import traceback

from django.db import DatabaseError
from django.utils.deprecation import MiddlewareMixin

from backend.exception.custom_exception import CustomException, ErrorCode
from backend.utils.api_response import response_failed, response_failed_base

ALLOW_PATHS = ["/api/users"]


class MyMiddleWare(MiddlewareMixin):
    """
    中间件，对请求统一处理
    """

    @staticmethod
    def process_request(request):
        """
        捕捉所有的请求
        """
        current_path = request.path
        if current_path in ALLOW_PATHS:
            pass
        else:
            user = request.user
            # 判断用户是否已经认证过了
            if user.is_authenticated:
                pass
            else:
                return response_failed(ErrorCode.UN_LOGIN)

    @staticmethod
    def process_response(request, response):
        """
        捕捉所有的响应
        """
        # print('获取到响应')
        return response

    @staticmethod
    def process_exception(request, exception):
        """
        捕捉所有的异常
        """
        # print('捕捉到异常了')
        print(traceback.print_exc())
        if isinstance(exception, CustomException):
            print('这是自定义错误')
            code = exception.code
            message = exception.message
            return response_failed_base(code, message)

        elif isinstance(exception, DatabaseError):
            print('数据库错误')
            return response_failed(ErrorCode.DB)
        else:
            print('未知错误')
            return response_failed(ErrorCode.UNKNOWN)
