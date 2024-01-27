from flask import Flask, render_template, request, redirect, session
import utility
import db_service

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'


def check_session():
    try: 
        if session['auth_id']:
            return True
    except:
        if 'auth_id' not in session:
            session['auth_id'] = None
    return False


def is_accessable(for_logged):
    if not check_session() and for_logged:
        return redirect("/login")
    elif check_session() and not for_logged:
        return redirect("/home")
    
    
@app.route("/")
def root():
    if not check_session():
        return redirect("/login")
    return redirect('/home')

@app.route('/login')
def login():
    if is_accessable(False):
        return is_accessable(False)
    error = request.args.get('error')
    return render_template("login.html", error=error, styles=['logreg'])

@app.route('/try_login', methods=['POST'])
def try_login():
    if is_accessable(False):
        return is_accessable(False)
    login = request.form['login']
    password = request.form['password']
    data = db_service.check_user(login, password)
    if data:
        session['auth_id'] = data[0]
        return redirect(f"/home")
    else:
        return redirect(f"/login?error=Wrong login or password")
@app.route('/register')
def register():
    if is_accessable(False):
        return is_accessable(False)
    error = request.args.get('error')

    return render_template("register.html", error=error, styles=['logreg'])

@app.route('/try_reg', methods=['POST'])
def try_reg():
    if is_accessable(False):
        return is_accessable(False)
    name = request.form['name']
    login = request.form['login']
    password = request.form['password']
    check_password = request.form['check_password']
    password_invalid = utility.check_password(password, check_password)
    login_invalid = db_service.check_login(login)
    if not (name and login and password and check_password):
        return redirect(f"/register?error=Fill in all fields")
    if login_invalid:
        return redirect(f"/register?error={login_invalid}")
    elif password_invalid:
        return redirect(f"/register?error={password_invalid}")
    else:
        db_service.add_user(name, login, password)
        return redirect("/login")

@app.route('/home')
def home():
    if is_accessable(True):
        return is_accessable(True)
    name = db_service.get_user(session['auth_id'])[1]
    posts = db_service.get_posts()
    return render_template("home.html", name=name, posts=posts, styles=['home', 'create'])

@app.route('/settings')
def settings():
    if is_accessable(True):
        return is_accessable(True)
    return render_template("settings.html", styles=['create'])

@app.route('/try_create', methods=['POST'])
def try_create():
    if is_accessable(True):
        return is_accessable(True)
    title = request.form['title']
    content = request.form['content']
    if not (title and content):
        return redirect(f"/settings?error=Fill in all fields")
    name = db_service.get_user(session['auth_id'])[1]
    db_service.add_post(name, title, content)
    return redirect("/home")

@app.route('/logout')
def logout():
    if is_accessable(True):
        return is_accessable(True)
    session['auth_id'] = None
    return redirect("/login")

@app.route('/account')
def account():
    if is_accessable(True):
        return is_accessable(True)
    name = db_service.get_user(session['auth_id'])[1]
    posts = db_service.get_user_posts(name)
    views = 0
    print(posts)
    return render_template(
        "account.html",
        name=name,
        posts=posts[::-1],
        styles=['account', 'create', 'home'],
        posts_len=len(posts),
        views=views,
    )

app.run(host="0.0.0.0")

