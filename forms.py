from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Email, Length


##WTForm
class ContactForm(FlaskForm):
    full_name = StringField("", validators=[DataRequired(), Length(min=3, max=120)], render_kw={"placeholder": "Full name"})
    email_address = EmailField("", validators=[Email()], render_kw={"placeholder": "Email address"})
    phone_number = StringField("", validators=[DataRequired()], render_kw={"placeholder": "Phone number"})
    message = TextAreaField("", validators=[DataRequired()], render_kw={"placeholder": "Message"})
    send = SubmitField("Send")
