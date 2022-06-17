from flask import Flask
from .models import db

app = Flask(__name__)
app.app_context().push()
app.secret_key = "inSpo_Eremyan2001-KubGu090601"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qummy_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
url_get = 'http://yarlikvid.ru:9999/api/top-secret-data'
url_post = 'http://yarlikvid.ru:9999/api/decrypt'
url_send = 'http://yarlikvid.ru:9999/api/result'
username = "qummy"
password = "GiVEmYsecReT!"

from .views import views

app.register_blueprint(views, url_prefix='/')

db.init_app(app)
db.create_all()
