from flask import Flask, render_template


app=Flask(__name__)

@app.route("/")
def home():
    courses=['python','react','django']
    student={"name":"Sneha"}


    return render_template("index.html",courses=courses,student=student)


if __name__=="__main__":
    app.run(debug=True) #once you start application, it will automatically run unless you dont manually end