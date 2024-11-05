from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    html = """
    <html>
       <body>
            <h1>Welcome to my website!</h1>
            <p>This is a simple website.</p>
            <a href="/hello">Say Hello</a>
        </body>
    </html>
"""
    return html


@app.route("/about")
def about():
    return "This is the about page"


@app.route("/hello")
def say_hello():
    return render_template("hello.html")


@app.route("/goodbye")
def say_goodbye():
    return "Goodbye, World!"


@app.route("/search")
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>You searched for:  {term}</h1> <p>Sorting by : {sort}</p>"


# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "This is a POST request"


# @app.route("/post", methods=["GET"])
# def post_demo():
#     return "This is a GET request"


@app.route("/add-comment")
def add_comment_form():
    return """
    <h1>Add Comment Form</h1>
    <form method="POST">
        <input type="text" name="comment" placeholder="Enter your comment">
        <input type="text" name="username" placeholder="Username">
        <button>Submit</button>
        </form>
    """


@app.route("/add-comment", methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    username = request.form["username"]
    print(request.form)
    return f"""
        <h1>SAVED YOUR COMMENT</h1>
        <ul>
            <li>Comment: {comment}</li>
            <li>Username: {username}</li>
        </ul>
    """


@app.route("/r/<subreddit>")
def show_subbredit(subreddit):
    return f"<h1>Browsing The {subreddit} Subreddit</h1>"


POSTS = {
    1: "I like chicken tenders",
    2: "I love eating pizza",
    3: "I hate spicy food",
    4: "I am a vegetarian",
}


@app.route("/posts/<int:id>")
def get_post(id):
    post = POSTS[id]
    return f"<h1>Post {id}</h1><p>{post}</p>"
