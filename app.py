from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['username']
        return redirect(url_for('home'))
    return '''
        <form method="post">
            <input name="username">
            <input type="submit">
        </form>
    '''

@app.route('/home')
def home():
    if 'user' in session:
        return f'hi my dear, {session["user"]}!'
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()