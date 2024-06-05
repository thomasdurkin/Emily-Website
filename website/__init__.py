from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = '6f5371ffabcc0f1c9ff9cb95554336f0'
app.config['MESSAGE_FLASHING_OPTIONS'] = {'duration': 5}

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'emilydurkinwebsite@gmail.com'
app.config['MAIL_RECIPIENT'] = 'emmied332@icloud.com'
app.config['MAIL_PASSWORD'] = 'hykafbdduvsygzxo'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail=Mail(app)

from website import routes