from flask import render_template , redirect , url_for , flash , request
from blog import app , db , becrypt
from blog.forms import LoginForm , RegistrationForm , UpdateProfileForm
from blog.models import User
from flask_login import login_user , current_user , logout_user , login_required
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register' , methods=['GET' , 'POST'])
def register():
    if current_user.is_authenticated:
        flash('you are loggined , please logout first and then register' , 'info')
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit(): #the custome validations in forms.py will be executed which are starting with validate ..
        username = form.username.data
        email = form.email.data
        password = form.password.data
        hashed_pass = becrypt.generate_password_hash(password).decode('utf-8')

        user = User(username = username , email = email , password = hashed_pass)

        db.session.add(user)
        db.session.commit()
        flash('you successfully registered' , 'success' )

        return redirect(url_for('home'))

    return render_template('register.html' , form = form)

@app.route('/login' , methods=['POST' , 'GET'])
def login():
    if current_user.is_authenticated:
        flash('you already have loggined' , 'info')
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and becrypt.check_password_hash(user.password , form.password.data):
            login_user(user , remember=form.remember.data)
            flash('you successfully logined ...' , 'success')
            next_page = request.args.get('next' , None)

            return redirect(next_page if next_page else url_for('home'))
        else :
            flash('email or passwrod wrong' , 'danger')


    return render_template('login.html' , form = form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you logged out successfully' , 'success')
    return redirect(url_for('home'))



@app.route('/profile' , methods=['POST' , 'GET'])
@login_required
def profile():
    form = UpdateProfileForm()

    if request.method =='POST' and form.validate_on_submit():
        
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('credentials updated' , 'success')
        return redirect(url_for('profile'))
    
    elif request.method == 'GET':

        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('profile.html' , form = form)