from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "Hello flasksss"


@app.route("/users")
def users():
    return "Welcome to user page"


@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"


@app.route("/student/<name>/<course>")
def student(name,course):
    return f"{name} has opted in for course {course}"


if __name__=="__main__":
    app.run(debug=True) #once you start application, it will automatically run unless you dont manually end