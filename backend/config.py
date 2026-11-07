import os

class Config:
    # Credenciais vêm de variáveis de ambiente (nunca commitar senhas/chaves).
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'mysql+pymysql://root:@localhost:3306/stockchef'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
