from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/upload', methods=['POST'])
def getInfo():
    if request.method == 'POST':
        data = [{'msg': "Hello Again"}]
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
