from flask import render_template, request, session, redirect, url_for

from . import auth_bp
from data_uzivatele import uzivatele
from .auth_service import AuthService

auth = AuthService(uzivatele)
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    chyba = None

    if request.method == 'POST':
        email = request.form.get('username', "")
        password = request.form('username', "")
        uzivatel = auth.prihlas(email, password)

        if uzivatel is None:
            session.clear()
            session['username_id'] = uzivatel.id

            return redirect(url_for('index'))


        chyba = "nesprávný email nebo heslo"

    return render_template('auth/login.html', chyba=chyba)