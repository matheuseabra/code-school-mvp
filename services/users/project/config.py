import os


class BaseConfig:
    """Base Env Configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_ENABLED = False              
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') 


class DevelopmentConfig:
    """Development Env Configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_DEV_URL')
    DEBUG_TB_ENABLED = True


class QAConfig:
    """QA Env Configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_QA_URL')


class ProductionConfig:
    """Production Env Configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_PROD_URL')
