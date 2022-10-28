from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = "6cc32ea8d819bd92e201e79a1207fef2"

posts = [
    {
        'author':'Mateusz Michalski',
        'title': 'Blog post1', 
        'content': 'First post content',
        'date_posted': '27.10.2022r.'
    },
    {
        'author':'random_nickname',
        'title': 'Blog post2', 
        'content': 'Second post content',
        'date_posted': '27.10.2022r.'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def register():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)