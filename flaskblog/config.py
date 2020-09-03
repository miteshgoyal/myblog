import os


class Config:
    SECRET_KEY = 'b6084bb84ec15aeb0ed32ac736568bc815d03e5f6829a91ae97e383b66a3e7b8c8adcd45442da596bb1ba5dcb1af36cdbcf4'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''