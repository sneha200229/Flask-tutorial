from flask import Flask, render_template
from uuid import UUID


app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True) #once you start application, it will automatically run unless you dont manually end