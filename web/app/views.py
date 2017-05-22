from web.webrun import app
from q_twitchbeagle import q_twitchbeagle
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    event = {
            'eventType' : 'electrical',
            'event'     : 'red toggle'
    }
    q_twitchbeagle.put(event)
    return "Hello, World!"

@app.route('/settings')
def settings():
    user = {
            'name' : 'Amp'
    }
    return render_template(
            'settings.html',
            title='Home',
            user=user)
