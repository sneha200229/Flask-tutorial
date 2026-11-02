from flask import Flask, render_template
from uuid import UUID


app=Flask(__name__)

@app.route("/")
def home():
    first_name="Sneha"
    last_name="Nandedkar"
    course=["Flask","python","django","fastAPI"]
    age=28
    price=500
    return render_template("index.html",course=course,age=age,price=price,first_name=first_name,last_name=last_name)


if __name__=="__main__":
    app.run(debug=True) #once you start application, it will automatically run unless you dont manually end