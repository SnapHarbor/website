from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/rating')
def rating_page():
    return render_template('rating.html')

@app.route('/players')
def players_page():
    return render_template('players.html')


if __name__ == '__main__':
    app.run()
