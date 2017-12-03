# ATS - Automated Trading Systems
This site will take in two stock tickers and a length of time. With this input it will...
1. Query Alpha Vantage (a stock API) and get the data for the two stocks over the specified length of time.
2. Remove any data that both stocks don't have. Alpha Vantage will sometimes be missing data for random times.
3. Find if the stocks are correlated. The stock times will be shifted against each other to see if they are more correlated at a certain time offset.
4. Make and display a graph of the two stocks over the entire time period.
5. Make and display a graph of the two stocks over their most correlated length of time.
6. Display correlation and offset data.

### API 

[Alpha Vantage](https://www.alphavantage.co/)

### Built With
Web Framework: [Flask](flask.pocoo.org), [wtforms](https://wtforms.readthedocs.io/en/latest/)

Graphing and Data Manipulation: numpy, pandas, matplotlib, others

### Authors
* **Daniel Ferriss** - *Web and Algorithm* - [github](https://github.com/danielferriss)
* **Divya Bhati** - *Graph and Algorithm* - [github](https://github.com/dbhati2)
* **Anmol Nigam** - *Algorithm* - [github](https://github.com/ANiggy)
* **Edward Park** - *Web and Algorithm* - [github](https://github.com/epark001)
* **Jarrett Brunner** - *Algorithm* - [github](https://github.com/jarrettbrunner)
* **Priyanka Dey** - *Graph and Algorithm* - [github](https://github.com/priyanka-dey)
* **Teja Kotha** - *Algorithm* - [github](https://github.com/tkotha99)
