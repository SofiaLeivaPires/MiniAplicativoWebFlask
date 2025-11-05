from flask import Flask, render_template, request, session, flash, redirect,url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

USERNAME = 'admin'
PASSWORD = '1234'

usuarios = [{"username": "admin", "password": "1234"}]

@app.route('/')
def home():
    # Quando for criado um login, cria-se um valor, gerando uma chave-valor
    # sessões ficam no cookies
    if "username" in session:
        return render_template('home.html', username=session['username'])

    return redirect(url_for('login'))

#
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        for user in usuarios:
            if user['username'] == username and user['password'] == password:
                session['username'] = username
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('home'))
        flash("Credenciais inválidas!", 'danger')
    return render_template('login.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        usuarios.append({"username": username, "password": password})

        flash('Cadastro realizado com sucesso!', 'success')


    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logout realizado com sucesso!', 'info')
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)