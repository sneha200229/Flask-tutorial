from flask import Flask, render_template
from uuid import UUID


app=Flask(__name__)

@app.route("/")
def home():
    name="Sneha"
    course="Flask"
    age=28
    return render_template("index.html",name=name,course=course,age=age)


if __name__=="__main__":
    app.run(debug=True) #once you start application, it will automatically run unless you dont manually end