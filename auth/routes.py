from flask import render_template, request, session, redirect, url_for

from . import auth_bp
from data_uzivatele import uzivatele
from .auth_service import AuthService

auth = AuthService(uzivatele)
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    chyba = None

    if request.method == 'POST':
        email = request.form.get('jmeno', "")
        password = request.form.get('password', "")

        uzivatel = auth.prihlas(email, password)

        if uzivatel is not None:
            session.clear()
            session['uzivatel_id'] = uzivatel.id
            session['uzivatel_jmeno'] = uzivatel.jmeno
            session['uzivatel_role'] = uzivatel.role



            return redirect(url_for('index'))


        chyba = "nesprávný email nebo heslo"

    return render_template('auth/login.html', chyba=chyba)