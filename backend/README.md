# 安装模块

- Django REST framework

```
pip install djangorestframework
pip install pymysql
pip install drf-yasg2
```

# 跨域问题

一般浏览器会阻止跨域的行为，设计在安全性上

后端解决跨域问题(不是好用，不推荐)：

1. 安装包：django-cors-headers(pip install django-cors-headers)
2. 项目目录下，settings中，添加app
    ```
    # Application definition

    INSTALLED_APPS = [
        ...
        'corsheaders',
    ]
    ```
3. 项目目录下，settings中，添加中间件('corsheaders.middleware.CorsMiddleware')，注意顺序
    ```
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware', # 添加上这个中间件
        'django.middleware.common.CommonMiddleware', # 注意顺序，必须是这个顺序（在这个之前添加中间件）
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ```
4. 项目目录下，settings中，添加跨域设置
    ```
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ORIGIN_WHITELIST = (
        '*'
    )
    
    CORS_ALLOW_METHODS = (
        'DELETE',
        'GET',
        'OPTIONS',
        'PATCH',
        'POST',
        'PUT',
        'VIEW',
    )
    
    CORS_ALLOW_HEADERS = (
        'XMLHttpRequest',
        'X_FILENAME',
        'accept-encoding',
        'authorization',
        'content-type',
        'dnt',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
        'Pragma',
    )
    ```

# 日志设置

项目目录下，settings中，添加如下内容 debug > info > warning > error

```
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'standard': {
            'format': ' [%(levelname)s] %(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] - %(message)s'}
    },
    'filters': {
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/all.log'),     #日志输出文件
            'maxBytes': 1024*1024*5,                  #文件大小
            'backupCount': 5,                         #备份份数
            'formatter':'standard',                   #使用哪种formatters日志格式
        },
        'error': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/error.log'),
            'maxBytes':1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'info': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/info.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        'django.request': {
            'handlers': [ 'default', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'interface': {
            'handlers': ['default', 'info',  'console', 'error'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
```

1. formatters: 配置打印日志格式
2. handler: 用来定义具体处理日志的方式，可以定义多种， "default"就是默认方式, "console"打印到控制台
3. loggers: 用来配置用那种handlers来处理日志，比如你同时需要输出日志到文件、控制台

# 定义接口格式

```
{
   "success": true,
   "data": [],
   "error": {
      "code": "error code"
      "message": "message"
   }
}
```

# 切换MySQL数据源

创建文件my.cnf内容如下：

```
[client]
host = 127.0.0.1
port = 3306
database = Name
user = USER
password = PASSWORD
default-character-set = utf8
```

在settings.py中将DATABASES修改为如下内容：

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'my.cnf')
         }
    }
}
```

初始化数据库：CREATE DATABASE bumblebee;

安装模块

```
python3 -m pip install pymysql
```

在项目的主目录下的`__init__.py`加入如下内容：

```
import pymysql

pymysql.install_as_MySQLdb()
```
