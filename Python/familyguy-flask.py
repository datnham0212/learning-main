from flask import Flask, abort
import pandas as pd

my_app = Flask(__name__)

@my_app.route('/')
def home():
    df = pd.read_html('https://en.wikipedia.org/wiki/List_of_Family_Guy_episodes#Episodes')
    return df[0].to_html()

@my_app.route('/Season <int:index>')
def get_seasons(index):
    df = pd.read_html('https://en.wikipedia.org/wiki/List_of_Family_Guy_episodes#Episodes')
    return df[index].to_html() if index <= 23 and index >= 0 else abort(404)


@my_app.route('/Specials')
def get_specials():
    df = pd.read_html('https://en.wikipedia.org/wiki/List_of_Family_Guy_episodes#Episodes')
    return df[25].to_html()

if __name__ == '__main__':
    my_app.run(debug=True)
