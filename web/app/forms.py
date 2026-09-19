from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class TwitchChannelForm(Form):
    channelName = StringField('channel')
    chatbotName = StringField('user')
    chatbotOauth = StringField('twitch_chat_oauth')

class TwitchAppForm(Form):


class LoginForm(Form):
        openid = StringField('openid', validators=[DataRequired()])
        remember_me = BooleanField('remember_me', default=False)
