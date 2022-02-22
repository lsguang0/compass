import os.path


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@192.168.2.255:3306/home'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # 项目路径               abspath 据对路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # 静态文件路径
    STATIC_DIR = os.path.join(BASE_DIR, 'static')


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
