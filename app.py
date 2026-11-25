from flask import Flask, render_template, session, redirect, url_for, abort
from main import main_bp
from data_uzivatele import uzivatele
from auth import auth_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = "zmen-me-na-nejaky-dlouhy-nahodny-retezec"
    app.register_blueprint(main_bp, url_prefix="/main")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/admin")
    def admin():
        if session.get('uzivatel_id') is None:
            return redirect(url_for('auth.login'))

        if session.get('uzivatel_role') != 'admin':
            abort(403)
        return render_template("admin.html", uzivatele=uzivatele)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)