from flask import Flask, render_template, request, redirect, url_for, flash
import random
import string
import pyperclip  
app = Flask(__name__)
app.secret_key = 'supersecretkey'
def generate_password(length, uppercase=True, lowercase=True, digits=True, symbols=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not any([uppercase, lowercase, digits, symbols]):
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
@app.route('/')
def index():
    return render_template('index1.html')
@app.route('/generate_password', methods=['POST'])
def generate_password_route():
    length = int(request.form['length'])
    uppercase = request.form.get('uppercase') == 'on'
    lowercase = request.form.get('lowercase') == 'on'
    digits = request.form.get('digits') == 'on'
    symbols = request.form.get('symbols') == 'on'

    password = generate_password(length, uppercase, lowercase, digits, symbols)
    pyperclip.copy(password)  
    flash('Password generated and copied to clipboard!')
    return render_template('index1.html', password=password)
if __name__ == '__main__':
    app.run(debug=True)
