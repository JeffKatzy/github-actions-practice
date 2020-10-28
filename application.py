from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    print('hola world')
    return "Hello Friend!"

# run the app.
if __name__ == "__main__":
    application.run()
