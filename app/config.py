# Created by Zhen-Yi Yu on 2024/03/19

import os

class Config:
    # Basic config
    SECRET_KEY = os.getenv("SECRET_KEY") or os.urandom(12)
    SYSTEM_FOLDER = os.getenv("REPO_DIR") or "./"


def get_config():
    # Fetch the flask_env from the environment variable
    env = os.getenv('SERVER_ENV')
    if env == 'Prod':
        print('Init with Prod config')
        return ProdConfig()
    elif env == 'Staging':
        print('Init with Staging config')
        return StagingConfig()
    elif env == 'Dev':
        print('Init with Dev config')
        return DevConfig()
    elif env == 'Test':
        print('Init with Test config')
        return TestConfig()
    # Return Dev config if without the parameter
    print('Init with Dev config')
    return DevConfig()
    
class ProdConfig(Config):
    # Production configuration
    FLASK_ENV = "Prod"

class StagingConfig(Config):
    # Stagging configuration
    FLASK_ENV = "Staging"

class DevConfig(Config):
    # Development configuration
    FLASK_ENV = "Dev"

class TestConfig(Config):
    # Testing configuration
    FLASK_ENV = "Test"
    TESTING = True