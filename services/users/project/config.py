
class BaseConfig:
    """Base Configuration"""
    TESTING = False

class DevelopmentConfig:
    """Development Configuration"""
    pass

class QAConfig:
    """QA Configuration"""
    TESTING = True

class ProductionConfig:
    """Production Configuration"""
    pass

