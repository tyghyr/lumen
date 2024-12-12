from flask import Flask, render_template,request,redirect
from pymongo import MongoClient

app = Flask(__name__)

isLoggedIn = False
credentials = { "shanks@gmail.com":"Shanks1","luffy@gmail.com":"luffy1"}

@app.route("/",methods=["GET","POST"])
def homepage():
    global isLoggedIn
    if request.method =="POST":
        log_email = request.form["mail"]
        log_password = request.form["pwd"]

        if (log_email in credentials) and (credentials[log_email]==log_password):
            isLoggedIn = True
            return redirect("/calci")
        else:
            return redirect("/")
    else:
        return render_template("login.html")

@app.route("/calci",methods=["GET","POST"])
def calculator():
    if isLoggedIn==True:
        if request.method=="POST":
            n1 = int(request.form["num1"])
            opr = request.form["opr"]
            n2 = int(request.form["num2"])
            if opr == "add":
                res = f"{n1} + {n2} is {n1+n2}"
                return render_template("index.html", output=res)
            elif opr == "sub":
                res = f"{n1} - {n2} is {n1-n2}"
                return render_template("index.html", output=res)
            elif opr == "mul":
                res = f"{n1} x {n2} is {n1*n2}"
                return render_template("index.html", output=res)
            elif opr == "div":
                try:
                    res = f"{n1} / {n2} is {n1/n2}"
                    return render_template("index.html", output=res)
                except Exception as e:
                    error = "Please change num2 as non-zero"
                    return render_template("index.html", output=error)
        else:
            return render_template("index.html")
    else:
        return redirect("/")
app.run(debug=True)