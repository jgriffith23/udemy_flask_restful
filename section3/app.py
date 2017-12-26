from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_home():
    return "Home"

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug = True
    app.run(port=5000)
