from flask import Flask
#app = Flask(__name__, template_folder='/root/twitch/twitch-sbc-integration/web/app/templates')
#app = Flask(__name__, template_folder='app/templates')
app = Flask(__name__)
from web.app import views

def web_handler():
    print app.template_folder
    app.run(host='0.0.0.0', threaded=True)
