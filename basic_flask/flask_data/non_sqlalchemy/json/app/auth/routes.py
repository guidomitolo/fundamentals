from app.main.models import User
from app.main.database import save_user, get_user_by_id, get_user_by_name, id_generator
from app.auth.forms import LoginForm, RegistrationForm
from app.auth import bp
from app import login_manager

from flask import render_template, flash, redirect, url_for

from flask_login import login_user, logout_user, login_required, current_user

from werkzeug.security import generate_password_hash, check_password_hash

@bp.route('/login', methods=["GET","POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()

    if form.validate_on_submit():

        try:
            user = get_user_by_name(form.username.data)
        except:
            flash('Invalid username')
            return redirect(url_for('auth.login'))

        if user is None:
            flash('Invalid username')
            return redirect(url_for('auth.login'))
        else:
            if check_password_hash(user.password, form.password.data) is False:
                flash('Invalid password')
                return redirect(url_for('auth.login'))
    
        login_user(user, form.remember_me.data)
        flash("Logged in!")
        return redirect(url_for('main.index'))

    return render_template('auth/login.html', title='Sign In', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("you are logged out")
    return redirect(url_for('auth.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()
    
    if form.validate_on_submit():
        try:
            if get_user_by_name(form.username.data) is not None:
                flash('Username already taken')
                return redirect(url_for('auth.register'))
            new_user = User(id_generator(), form.username.data, form.email.data, generate_password_hash(form.password.data, method='sha256'))
            save_user(new_user)
            login_user(new_user)
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('main.index'))
        except:
            new_user = User(id_generator(), form.username.data, form.email.data, generate_password_hash(form.password.data, method='sha256'))
            save_user(new_user)
            login_user(new_user)
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('main.index'))

    return render_template('auth/register.html', title='Register', form=form)

@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)