'''
Created 27 October 2022
'''

from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)

