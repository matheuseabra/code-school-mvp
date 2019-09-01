import os


class BaseConfig:
    """Base Env Configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig:
    """Development Env Configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_DEV_URL')


class QAConfig:
    """QA Env Configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_QA_URL')


class ProductionConfig:
    """Production Env Configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_PROD_URL')
