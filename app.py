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
        name=request.form.get("name").strip()
        email=request.form.get("email").strip()
        age=request.form.get("age").strip()
        if not name:
            return "Name is required"
        if not email:
            return "Email is required"
        if not age:
            return "Age is required"
        if not age.isdigit():
            return "Age must be numberS"
        return "Registration successsful"
        # message=request.form["message"] #can give key error#
        return f"Hello {name}, your email is {email} and age id {age} "
    return render_template("contact.html")#name=name



if __name__=="__main__":
    app.run(debug=True) #once you start application, it will automatically run unless you dont manually end