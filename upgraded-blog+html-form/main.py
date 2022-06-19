from flask import Flask, render_template, request
import requests
import smtplib
import os


TO_EMAIL = os.environ["to_email"]
FROM_EMAIL = os.environ["from_email"]
EMAIL_PASSWORD = os.environ["email_app_password"]


app = Flask(__name__)

# Fetch API Data
response = requests.get("https://api.npoint.io/9026f703da2055b1ab8b")
data = response.json()


@app.route("/")
def main():
    return render_template("index.html", posts=data, length=len(data))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    request_method = request.method
    if request.method == "GET":
        return render_template("contact.html", method=request_method)

    elif request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        # SEND EMAIL

        with smtplib.SMTP("smtp.gmail.com") as smtp:
            smtp.starttls()
            smtp.login(user=FROM_EMAIL, password=EMAIL_PASSWORD)
            smtp.sendmail(
                from_addr=FROM_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"POST REQUEST\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}\n")

        return render_template("contact.html", method=request_method)


@app.route("/post/<num>")
def post(num):
    num = int(num)
    return render_template("post.html", post_num=num, posts=data)


if __name__ == "__main__":
    app.run(debug=True)

