from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


## 增加 /health 供Eureka检查服务状态
@app.route('/health')
def health():
    return jsonify({
        'status': 'UP'
    })


if __name__ == '__main__':
    app.run()
