from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return("This is sparta!or is it!!!")

@app.route("/admin")
def hello_admin():
    return("admin it is!!!!!!")
app.run()