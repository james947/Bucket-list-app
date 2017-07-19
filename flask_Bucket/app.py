from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key= '\x9a\x9fc!\x00\x14\xbf\n\xd6\xfa\xbf\xaf\xb7\xdc]\x0c~\\\x01L\xbe:\x05W'


@app.route('/')
def index():
    return 'hello world'
#starts user session
@app.route('/login', methods=['GET','POST'] )
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'user' and request.form['password'] != 'user':
            error ='invalid credentials.please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('bucket'))
    return  render_template("login.html", error = error)

@app.route('/bucket')
def bucket():
    return render_template("bucketlist.html")

@app.route('/register')
def register():
    return  render_template("register.html")
#Ends the session
@app.route('/logout')
def logout():
    session.pop('logged in', None)
    return redirect(url_for('login'))


if __name__== '__main__':
    app.run(debug='True')

