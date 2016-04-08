from flask import Flask, url_for, render_template
app = Flask(__name__)
app.debug = True

@app.route("/index")
@app.route("/")
def display_index():
    return render_template("index.html", page_title="Lorem")

@app.route("/login")
def display_login():
    return render_template("login.html", page_title="Login")

@app.route("/register")
def display_register():
    return render_template("register.html", page_title="Register")

@app.route("/donations")
def display_donations():
    return "donations"

if __name__ == "__main__":
    app.run()

