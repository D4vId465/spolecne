from flask import Flask
from main.routes import main_bp
app = Flask(__name__)

#Registrace Blueprintu
app.register_blueprint(main_bp)

@app.route("/about")
def about():
    return "<h1>O aplikaci</h1>"

if __name__ == "__main__":
    app.run(debug=True)