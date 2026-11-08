
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>User Registration Form</h2>
    <form action="/register" method="post">
        Name: <input type="text" name="name" required><br><br>
        Email: <input type="email" name="email" required><br><br>
        Password: <input type="password" name="password" required><br><br>
        <input type="submit" value="Register">
    </form>
    '''

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']

    return f'''
    <h2>Registration Successful!</h2>
    <p>Welcome, {name}!</p>
    <p>Email: {email}</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
