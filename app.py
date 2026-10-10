from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "Hello flasksss"

if __name__=="__main__":
    app.run(debug=True) #once you start application, it will automatically run unless you dont manually end