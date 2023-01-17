from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from forms import ContactForm
from flask_bootstrap import Bootstrap
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("APP_SECRET_KEY")
Bootstrap(app)

MY_EMAIL = os.environ.get("EMAIL_ADDRESS")
MY_PASSWORD = os.environ.get("EMAIL_PASSWORD")


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()
    if request.method == 'POST':
        sender = request.form["full_name"]
        sender_email = request.form["email_address"]
        sender_phone_number = request.form["phone_number"]
        sender_message = request.form["message"]

        with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="sas.peter.hu@gmail.com",
                msg=f"Subject:Message from your portfolio website\n\nFull name: {sender}\n"
                    f"Email address: {sender_email}\nPhone number: {sender_phone_number}\n\n"
                    f"Message:\n{sender_message}"
            )
        flash("Message sent")
        return redirect(url_for('home')+"#contact")
    return render_template("index.html", now=datetime.utcnow(), form=form)



if __name__=="__main__":
    app.run(debug=True)