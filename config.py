# config.py
import os

class Config:
    # Configurações do Flask base e SQLAlchemy
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///seloedu.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- NOVO: Configurações do Flask-Mail para usar o MailHog ---
    MAIL_SERVER = '127.0.0.1'  # Endereço padrão do MailHog
    MAIL_PORT = 1025           # Porta SMTP padrão do MailHog
    MAIL_USE_TLS = False       # Não é necessário TLS/SSL para MailHog local
    MAIL_USE_SSL = False
    MAIL_USERNAME = ''         # Não é necessário autenticação no MailHog
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = 'noreply@seloedu.com' # Email de envio padrão