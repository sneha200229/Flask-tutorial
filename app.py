from flask import Flask
from uuid import UUID
app=Flask(__name__)
@app.route("/")
def home():
    return "Hello flasksss"


@app.route("/users/<uuid:id>")
def users(id):
    return str(id)


@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"


@app.route("/student/<name>/<int:roll>")
def student(name,roll):
    return f"{name} has roll number {roll}"


@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

if __name__=="__main__":
    app.run(debug=True) #once you start application, it will automatically run unless you dont manually end