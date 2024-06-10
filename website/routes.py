from flask import render_template, request, flash, url_for, redirect
from flask_mail import Message
from website import app, mail

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/gallery")
def gallery():
	return render_template('gallery.html')\

@app.route("/media")
def media():
	return render_template('media.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/resume")
def resume():
	return render_template('resume.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
	if request.method == "POST":
		form_data = request.form.to_dict()

		msg = Message(
			subject = form_data['subject'],
			sender = app.config['MAIL_USERNAME'],
			recipients = [app.config['MAIL_RECIPIENT']]
		)

		msg.html = f"""<div> 
							{ form_data['message'] } 
						</div>
						<br>
						<div>
							{ form_data['email'] } 
						</div>
						<br>
						<div>
							{ form_data['name'] } 
						</div>"""
		
		mail.send(msg)
		flash('Your message has been sent!', 'success')
		return redirect(url_for('contact'))

	else:
		return render_template('contact.html')