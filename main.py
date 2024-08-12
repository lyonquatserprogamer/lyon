from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

main = Flask(__name__)
main.config['SECRET_KEY'] = 'lyon2010,'  # Cambia esto por una clave secreta aleatoria y segura
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(main)
migrate = Migrate(main, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    nickname = db.Column(db.String(150), unique=True, nullable=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

class RegisterForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6, max=150)])
    nickname = StringField('Apodo', validators=[Length(max=150)])
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')

@main.route('/')
def home():
    users = User.query.all()
    return render_template('home.html', users=users)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nickname = request.form.get('nickname')
        
        # Verificar si el nombre de usuario o apodo ya existen
        existing_user = User.query.filter((User.username == username) | (User.nickname == nickname)).first()
        
        if existing_user:
            return 'El nombre de usuario o apodo ya está en uso', 400
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password, nickname=nickname)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('home'))  # Redirige a la página de inicio

        return 'Inicio de sesión fallido', 401  # Código de estado HTTP 401 para fallos de autenticación

    return render_template('login.html')

@main.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Has cerrado sesión')
    return redirect(url_for('home'))

@main.route('/forum', methods=['GET', 'POST'])
def forum():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        content = request.form['content']
        new_post = Post(content=content, user_id=session['user_id'])
        db.session.add(new_post)
        db.session.commit()

    posts = Post.query.all()
    return render_template('forum.html', posts=posts)

@main.route('/info')
def info():
    return render_template('info.html')

if __name__ == "__main__":
    main.run(debug=True)