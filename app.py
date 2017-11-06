from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'reallyreallyreallyreallysecretkey'
print('I will kill you Danny -Ann')


manager   = Manager(app)
bootstrap = Bootstrap(app)
moment    = Moment(app)

class TickerForm(FlaskForm):
    ticker1   = StringField(u'Ticker 1:',     validators=[Required()])
    ticker2   = StringField(u'Ticker 2:',     validators=[Required()])
    length    = SelectField(u'Time Length:', choices=[('1day', '1 day'), ('1week', '1 week'), ('2week', '2 weeks'), ('10week', '10 weeks'), ('1year', '1 year')])
    interval  = SelectField(u'Time Interval:', choices=[('1', '1 second'), ('1 minute', '1 minute'), ('text', '1 hour'), ('text', '1 day')])
    submit    = SubmitField(u'Submit')

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
    app.run()
