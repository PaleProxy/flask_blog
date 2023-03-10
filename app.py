from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {'author': 'Boop Snoot',
     'title': 'Blog Post 1',
     'content': 'First post ever',
     'date_posted': 'March 8 2023'
    },
    {
     'author': 'Bam Boozle',
     'title': 'Blog Post 2',
     'content': 'Second post ever',
     'date_posted': 'March 9 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',
                           posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)