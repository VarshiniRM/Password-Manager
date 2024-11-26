from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
db = SQLAlchemy(app)

# Generate and store encryption key securely
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Password model
class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    password_encrypted = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        passwords = Password.query.filter_by(user_id=session['user_id']).all()
        return render_template('dashboard.html', passwords=passwords)
    return redirect(url_for('login'))

@app.route('/add_password', methods=['GET', 'POST'])
def add_password():
    if 'user_id' in session:
        if request.method == 'POST':
            site = request.form['site']
            username = request.form['username']
            password = request.form['password']
            encrypted_pw = cipher_suite.encrypt(password.encode('utf-8'))
            
            new_password = Password(site=site, username=username, password_encrypted=encrypted_pw, user_id=session['user_id'])
            db.session.add(new_password)
            db.session.commit()
            return redirect(url_for('dashboard'))
        return render_template('add_password.html')
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():  # Add this line
        db.create_all()       # This ensures the context is active
    app.run(debug=True)       # Keep this line outside the context


