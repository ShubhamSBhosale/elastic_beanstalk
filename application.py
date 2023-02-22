from flask import Flask

application = Flask(__name__)  # This needs to be named `application`


@application.route('/')
def hello():
    return 'Hello, World! V2'


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
