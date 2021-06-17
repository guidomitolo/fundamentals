from app.main.models import User, UsersRepo
from app.auth.forms import LoginForm, RegistrationForm

# login_manager is initialized after the creation of the app
from app import login_manager

from app.auth import bp

from flask_login import login_user, logout_user, login_required, current_user

from flask import render_template, flash, redirect, url_for

# users repository call to persist users data in flask running
users_repository = UsersRepo()

@bp.route('/login', methods=["GET","POST"])
def login():
    # check if there is an user already logged on
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    # call the login form
    form = LoginForm()
    # validate forms with wtforms
    if form.validate_on_submit():
        # call the users repository to check data and then login
        registeredUser = users_repository.get_user_by_name(form.username.data)
        if registeredUser is None:
            flash('Invalid username')
            return redirect(url_for('auth.login'))
        if registeredUser.password != form.password.data:
            flash('Invalid password')
            return redirect(url_for('auth.login'))
            
        login_user(registeredUser, form.remember_me.data)
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
        if users_repository.get_user_by_name(form.username.data) is not None:
            flash('Username already taken')
            return redirect(url_for('auth.register'))
        new_user = User(form.username.data, form.password.data, str(users_repository.next_index()))
        users_repository.save_user(new_user)
        
        # login once the registration process is completed
        login_user(new_user)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', title='Register', form=form)

# load user is called after the object user is instantiated
@login_manager.user_loader
def load_user(user_id):
    return users_repository.get_user_by_id(user_id)