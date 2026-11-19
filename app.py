from flask import Flask, render_template,request


app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method=="POST":
        name=request.form.get("username")
        email=request.form.get("email")
        message=request.form["message"] #can give key error#
        return f"Hello {name}, your email is {email} and message is {message}"
    return render_template("contact.html",name=name)



if __name__=="__main__":
    app.run(debug=True) #once you start application, it will automatically run unless you dont manually end