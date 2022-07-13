from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def number_games():
    return render_template('number_games.html')

if __name__ == "__main__":
    app.run()