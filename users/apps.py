from django.apps import AppConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import datetime
from flask_login import UserMixin
from flask_security import RoleMixin
# from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

# Модель пользователя
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/favicon.ico')
def favicon():
    return '', 204

# Регистрация
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         user = User.query.filter_by(username=username).first()
#         if user:
#             flash('Пользователь с таким именем уже существует')
#             return redirect(url_for('register'))
#         new_user = User(username=username, password=password)
#         db.session.add(new_user)
#         db.session.commit()
#         flash('Регистрация прошла успешно! Войдите в систему.')
#         return redirect(url_for('login'))
#         return render_template('register.html')
#


# Вход в систему
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         user = User.query.filter_by(username=username).first()
#         if user and user.password == password:
#             login_user(user)
#             return redirect(url_for('dashboard'))
#         flash('Некорректные учетные данные')
#     return render_template('login.html')

# Защищённая страница
# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return f'Добро пожаловать, {current_user.username}!'
#
# # Выход
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))
#
# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)