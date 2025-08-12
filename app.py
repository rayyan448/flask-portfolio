from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    print(f"New contact form submission: {name}, {email}, {message}")
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)
