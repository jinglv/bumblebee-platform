class ErrorCode:
    """
    预定义错误码与错误信息
    """
    # 系统错误
    SYSTEM = {"10000": "系统错误"}
    # 数据库错误
    DB = {"20000": "数据库错误"}
    # 参数错误
    COMMON = {"30000": "参数错误"}
    # 未知错误
    UNKNOWN = {"40000": "数据库错误"}

    UN_LOGIN = {"10001": "用户未登录"}
    USER_LOGIN_FAIL = {"10002": "用户登录失败"}
    USER_EXIST = {"10003": "用户已存在"}
    REGISTER_FAIL = {"10004": "注册失败"}
    USER_OR_PWD_NULL = {"10010": "用户名或密码为空"}
    USER_OR_PWD_ERROR = {"10011": "用户名或密码错误"}
    PWD_ERROR = {"10012": "两次密码不一致"}

    PROJECT_NAME_EXIST = {"10021": "项目名称已存在"}
    PROJECT_NOT_EXIST = {"10022": "项目不存在"}
    PROJECT_IS_DELETE = {"10023": "项目已删除"}
    IMAGE_SUFFIX_ERROR = {"10024": "上传图片格式错误"}
    IMAGE_SIZE_ERROR = {"10024": "图片大小不能超过2MB"}
    JSONPATH_ERROR = {"10025": "JsonPath未能匹配到值"}

    MODULE_NAME_EXIST = {"10031": "项目中已存在模块名称"}
    MODULE_NO_EXIST = {"10032": "项目中模块不存在"}
    MODULE_IS_DELETE = {"10033": "项目模块已删除"}

    CASE_PARAMS_ERROR = {"10041": "用例传入参数类型错误"}
    CASE_IS_DELETE = {"10042": "测试用例已删除"}
    CASE_EXTRACT_ERROR = {"10043": "提取器校验失败"}

    BASE_DATA_TYPE_ERROR = {"10051": "基础数据类型错误"}
    SCENE_DATA_TYPE_ERROR = {"10052": "场景数据类型错误"}
    DATA_TYPE_NAME_EXIST = {"10053": "数据类型名称已存在"}

    TASK_IS_DELETE = {"10061": "测试任务已删除"}
    CASE_NOT_EXIST = {"10062": "测试用例不存在"}


class CustomException(Exception):
    def __init__(self, error=None):
        if error is None:
            error = ErrorCode.COMMON
        self.message = list(error.values())[0]
        self.code = list(error.keys())[0]

    def __str__(self):
        return self.message
