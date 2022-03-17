from flask import (
    Blueprint, current_app, flash, redirect, render_template, request, url_for
)
from . import db
import sendgrid
from sendgrid.helpers.mail import *

bp = Blueprint('mail', __name__, url_prefix="/" )

@bp.route("/", methods=["GET"])
def index():
    search = request.args.get("search")
    g,c = db.get_db()
    if search is None:
        data = c.execute("SELECT * FROM email")
    else:
        data = c.execute("SELECT * FROM email WHERE content like %s", ('%' + search + '%', ))
    mails = c.fetchall()
    return render_template("mails/index.html", mails=mails)

@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":                    #si es POST
        email = request.form.get("email")           #tomamos los archivos del form
        subject = request.form.get("subject")
        content = request.form.get("content")
        errors = []                                 #creamos una lista de errores y los vamos agregando

        if not email:
            errors.append("Email es obligatorio")   
        if not subject:
            errors.append("Subject es obligatorio")   
        if not content:
            errors.append("Content es obligatorio")   
        
        if len(errors) == 0: 
            send(email, subject, content)                       #si no hay errores
            g,c = db.get_db()
            c.execute("INSERT INTO email (email, subject, content) VALUES (%s,%s,%s)", (email,subject,content))
            g.commit()
            return redirect(url_for("mail.index"))
        else:
            for error in errors:                    #si hay errores se los mostramos al usaurio
                flash(error)    
   
    return render_template("mails/create.html")

def send(to,subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_API_KEY'])
    from_email = Email(current_app.config['FROM_EMAIL'])
    to_email = To(to)
    contents = Content('text/plain', content)
    mails = Mail(from_email, to_email, subject, contents)
    response = sg.client.mail.send.post(request_body=mails.get())
    print(response)