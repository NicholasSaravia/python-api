from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def gree_user():
    return jsonify({'message': 'Hello Wold'})

if __name__ == '__main__':
    app.run(debug=True)