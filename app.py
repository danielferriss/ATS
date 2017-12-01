from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required
from flask_navigation import Navigation
from algo import *

app = Flask(__name__)
nav = Navigation(app)
app.config['SECRET_KEY'] = 'reallyreallyreallyreallysecretkey'


manager   = Manager(app)
bootstrap = Bootstrap(app)
moment    = Moment(app)

class TickerForm(FlaskForm):
    ticker1   = StringField(u'Ticker 1:', validators=[Required()])
    ticker2   = StringField(u'Ticker 2:', validators=[Required()])
    length    = SelectField(u'Time Length:', choices=[('', ''),('1day', '1 day'), ('1week', '1 week'), ('2week', '2 weeks'), ('10week', '10 weeks'), ('1year', '1 year')])
    submit    = SubmitField(u'Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    ticker1  = None
    ticker2  = None
    length   = None
    graph    = None
    form     = TickerForm()
    if form.validate_on_submit():
        ticker1  = form.ticker1.data
        ticker2  = form.ticker2.data
        length   = form.length.data
        graph    = stockchart(ticker1, ticker2)
        return render_template('index.html', form=form, ticker1=ticker1, ticker2=ticker2, length=length, graph = graph)
    return render_template('index.html', form=form, ticker1=ticker1, ticker2=ticker2, length=length, graph = graph)

@app.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('team.html')

@app.route('/algorithm', methods=['GET', 'POST'])
def algorithm():
    return render_template('algorithm.html')

@app.route('/news', methods=['GET', 'POST'])
def news():
    return render_template('news.html')

if __name__ == '__main__':
    app.run()
