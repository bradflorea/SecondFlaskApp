from flask import Flask

app = Flask(__name__)


@app.route("/")
def say_hello():
    html = """
    <html>
     <body>
     <h1>Hello, World!</h1>
      <p>This is a simple Flask application.</p>
     </body>
    </html>
    """
    return html


@app.route("/goodbye")
def say_goodbye():
    return "Goodbye, World!"
