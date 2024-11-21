from  flask import Flask,jsonify

app = Flask(__name__)

@app.route('/main')
def hello_world():
    return jsonify({
        'message':'hello world'
    })


if __name__=='__main__':
    app.run()