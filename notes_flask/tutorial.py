from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method =="POST":
        return redirect(url_for("user", name=request.form["name"]))
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/<name>")
def user(name):
    return f"<p>hello {name}!<?p>"

if __name__== "__main__":
    app.run(debug=True)



    #jl flask notes 7th

#What does Flask do?
    #allows us to have multipgae websites that is imported from python

#What are the steps to setting up a Flask project?
    #we have routes to show different pages based on adding different info to the routes

#How can you reference subpages on your Flask project? (Meaning the difference between the home page and a personal profile)
    #you change the url

#What are templates?
    #a cookie cutter to make multiple pages with the same stuff