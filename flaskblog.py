from flask import Flask, render_template
app = Flask(__name__)

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
    return render_template('about.html', title="about")


if __name__ == '__main__':
    app.run(debug=True)