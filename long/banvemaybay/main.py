from flask import render_template
from banvemaybay import banvemaybay

@banvemaybay.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    banvemaybay.run(debug=True)