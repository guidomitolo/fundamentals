from app.models import User, UsersRepo
from app.forms import LoginForm, RegistrationForm
from app import app, login_manager

from flask_login import login_user, logout_user, login_required, current_user

from flask import render_template, request, redirect, flash, url_for

# users repository call to persist users data in flask running
users_repository = UsersRepo()

@app.route('/login', methods=["GET","POST"])
def login():
    # check if there is an user already logged on
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # call the login form
    form = LoginForm()
    # validate forms with wtforms
    if form.validate_on_submit():
        # call the users repository to check data and then login
        registeredUser = users_repository.get_user_by_name(form.username.data)
        if registeredUser is None:
            flash('Invalid username')
            return redirect(url_for('login'))
        if registeredUser.password != form.password.data:
            flash('Invalid password')
            return redirect(url_for('login'))
            
        login_user(registeredUser, form.remember_me.data)
        flash("Logged in!")
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("you are logged out")
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()

    if form.validate_on_submit():
        if users_repository.get_user_by_name(form.username.data) is not None:
            flash('Username already taken')
            return redirect(url_for('register'))
        new_user = User(form.username.data, form.password.data, str(users_repository.next_index()))
        users_repository.save_user(new_user)
        
        # login once the registration process is completed
        login_user(new_user)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html")

# load user is called after the object user is instantiated
@login_manager.user_loader
def load_user(user_id):
    print('user loader/ load user function call.')
    print('input id:',user_id)
    print('user object with input id:',users_repository.get_user_by_id(user_id))
    return users_repository.get_user_by_id(user_id)