#           _____                _____                     _____          
#          /\    \              /\    \                    /\    \         
#         /::\    \            /::\    \                  /::\    \        
#        /::::\    \           \:::\    \                /::::\    \       
#       /::::::\    \           \:::\    \              /::::::\    \      
#      /:::/\:::\    \           \:::\    \            /:::/\:::\    \     
#     /:::/__\:::\    \           \:::\    \          /:::/__\:::\    \    
#    /::::\   \:::\    \          /::::\    \         \:::\   \:::\    \   
#   /::::::\   \:::\    \        /::::::\    \      ___\:::\   \:::\    \  
#  /:::/\:::\   \:::\    \      /:::/\:::\    \    /\   \:::\   \:::\    \ 
# /:::/  \:::\   \:::\____\    /:::/  \:::\____\  /::\   \:::\   \:::\____\
# \::/    \:::\  /:::/    /   /:::/    \::/    /  \:::\   \:::\   \::/    /
#  \/____/ \:::\/:::/    /   /:::/    / \/____/    \:::\   \:::\   \/____/ 
#           \::::::/    /   /:::/    /              \:::\   \:::\    \     
#            \::::/    /   /:::/    /                \:::\   \:::\____\    
#            /:::/    /    \::/    /                  \:::\  /:::/    /    
#           /:::/    /      \/____/                    \:::\/:::/    /     
#          /:::/    /                                   \::::::/    /      
#         /:::/    /                                     \::::/    /       
#         \::/    /                                       \::/    /        
#          \/____/                                         \/____/         
#
# .----------------.  .-----------------. .----------------.                     
#| .--------------. || .--------------. || .--------------. |                    
#| |     ___      | || | ____  _____  | || |     ____     | |                    
#| |    / _ \     | || ||_   \|_   _| | || |   .'    `.   | |                    
#| |   |_/ \_|    | || |  |   \ | |   | || |  /  .--.  \  | |                    
#| |              | || |  | |\ \| |   | || |  | |    | |  | |                    
#| |              | || | _| |_\   |_  | || |  \  `--'  /  | |                    
#| |              | || ||_____|\____| | || |   `.____.'   | |                    
#| |              | || |              | || |              | |                    
#| '--------------' || '--------------' || '--------------' |                    
# '----------------'  '----------------'  '----------------'                     
# .----------------.  .----------------.  .----------------.  .----------------. 
#| .--------------. || .--------------. || .--------------. || .--------------. |
#| |   _____      | || |     _____    | || |  _________   | || |  _________   | |
#| |  |_   _|     | || |    |_   _|   | || | |_   ___  |  | || | |_   ___  |  | |
#| |    | |       | || |      | |     | || |   | |_  \_|  | || |   | |_  \_|  | |
#| |    | |   _   | || |      | |     | || |   |  _|      | || |   |  _|  _   | |
#| |   _| |__/ |  | || |     _| |_    | || |  _| |_       | || |  _| |___/ |  | |
#| |  |________|  | || |    |_____|   | || | |_____|      | || | |_________|  | |
#| |              | || |              | || |              | || |              | |
#| '--------------' || '--------------' || '--------------' || '--------------' |
# '----------------'  '----------------'  '----------------'  '----------------' 


from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, AnyOf
from flask_navigation import Navigation
from algo import *       


app = Flask(__name__)
nav = Navigation(app)
app.config['SECRET_KEY'] = 'reallyreallyreallyreallysecretkey'


manager   = Manager(app)
bootstrap = Bootstrap(app)
moment    = Moment(app)
choices   = [('', ''),('1day', '1 day'), ('1week', '1 week'), ('4week', '4 weeks'), ('3month', '3 months'), ('1year', '1 year'), ('5year', '5 years')]

class TickerForm(FlaskForm):
    ticker1   = StringField(u'Ticker 1:',    validators=[Required(), AnyOf(symbols(), message=u'Ticker 1 is not a valid symbol!')])
    ticker2   = StringField(u'Ticker 2:',    validators=[Required(), AnyOf(symbols(), message=u'Ticker 2 is not a valid symbol!')])
    length    = SelectField(u'Time Length:', validators=[Required()], choices=choices)
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
        graph    = stockchart(ticker1, ticker2, length)
        tickerlate = 'tickerlate'
        tickerearly = 'tickerearly'
        correlation = 'correlation'
        offset = 'offset'
        return render_template('index.html', form=form, ticker1=ticker1, ticker2=ticker2, length=length, graph = graph, tickerlate=tickerlate, tickerearly=tickerearly, correlation=correlation, offset=offset)
    return render_template('index.html', form=form, ticker1=ticker1, ticker2=ticker2, length=length, graph = graph)

@app.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('team.html')

@app.route('/algorithm', methods=['GET', 'POST'])
def algorithm():
    return render_template('algorithm.html')

@app.route('/news', methods=['GET', 'POST'])
def news():
    return render_template('news.html', ticker1 = 'GOOGL', ticker2 = 'MSFT')

if __name__ == '__main__':
    app.run()
