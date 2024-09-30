from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def say_hello():
    html = """
    <html>
     <body>
     <h1>Hello, World!</h1>
      <p>This is the hello page.</p>
     </body>
    </html>
    """
    return html


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
        <button>Submit</button>
        </form>
    """


@app.route("/add-comment", methods=["POST"])
def save_comment():
    return """
    <h1>Comment saved!</h1>
    """
