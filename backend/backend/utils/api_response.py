from django.http import JsonResponse

from backend.exception.custom_exception import ErrorCode


def response_json(success, error_code, message, data):
    result = dict()
    result["success"] = success
    result["error"] = {
        "code": error_code,
        "message": message
    }
    result["data"] = data
    return JsonResponse(result, safe=False)


def response_success(data=None):
    if data is None:
        data = {}
    return response_json(True, "", "", data)


def response_failed(error=ErrorCode.COMMON):
    error_code = list(error.keys())[0]
    error_message = list(error.values())[0]
    return response_json(False, error_code, error_message, {})


def response_failed_base(code, message):
    return response_json(False, code, message, {})
