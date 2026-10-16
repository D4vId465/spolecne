from flask import Flask, render_template
from main import main_bp
from data_uzivatele import uzivatele
from auth import auth_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp, url_prefix="/main")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/admin")
    def admin():
        return render_template("admin.html", uzivatele=uzivatele)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)