from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'reallyreallyreallyreallysecretkey'

manager   = Manager(app)
bootstrap = Bootstrap(app)
moment    = Moment(app)

class TickerForm(FlaskForm):
    ticker1   = StringField('Ticker 1:',     validators=[Required()])
    ticker2   = StringField('Ticker 2:',     validators=[Required()])
    interval  = StringField('Time Interval:', validators=[Required()])
    length    = StringField('Time Length:',  validators=[Required()])
    submit    = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    ticker1  = None
    ticker2  = None
    interval = None
    length   = None
    form = TickerForm()
    if form.validate_on_submit():
        ticker1  = form.ticker1.data
        ticker2  = form.ticker2.data
        interval = form.interval.data
        length   = form.length.data
    return render_template('index.html', form=form, ticker1=ticker1, ticker2=ticker2, interval=interval, length=length)

if __name__ == '__main__':
