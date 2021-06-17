from app.models import User
from app.auth.forms import LoginForm, RegistrationForm
from app.auth import bp
from app import login_manager

from app.database import Query

from flask import render_template, flash, redirect, url_for

from flask_login import login_user, logout_user, login_required, current_user

@bp.route('/login', methods=["GET","POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    db = Query()

    if form.validate_on_submit():

        user = db.select_by_name(form.username.data)

        if user is None:
            flash('Invalid username')
            return redirect(url_for('auth.login'))
        else:
            if db.check_password(form.password.data) is None:
                flash('Invalid password')
                return redirect(url_for('auth.login'))
    
        login_user(User(user['id'], user['username'], user['email'], user['password']), form.remember_me.data)
        flash("Logged in!")
        return redirect(url_for('index'))

    return render_template('auth/login.html', title='Sign In', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You are logged out")
    return redirect(url_for('auth.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    db = Query()
    
    if form.validate_on_submit():
        if db.select_by_name(form.username.data) is not None:
            flash('Username already taken')
            return redirect(url_for('auth.register'))

        if db.check_email(form.email.data) is not None:
            flash('Email already taken')
            return redirect(url_for('auth.register'))
       
        db.insert_user(form.username.data, form.email.data, form.password.data)

        # need to get the recently inserted row to borrow id
        new_user = db.select_by_name(form.username.data)

        login_user(User(new_user['id'], new_user['username'], new_user['email'], new_user['password']))
        return redirect(url_for('index'))

    return render_template('auth/register.html', title='Register', form=form)

@login_manager.user_loader
def load_user(user_id):
    db = Query()
    log_user = db.select_by_id(user_id)
    user = User(log_user['id'], log_user['username'], log_user['email'], log_user['password'])
    return user