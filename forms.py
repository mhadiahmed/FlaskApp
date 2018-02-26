from wtforms import Form, StringField, PasswordField,TextAreaField,validators

class RigesterForm(Form):
	name = StringField('Name',[validators.Length(min=4,max=20)])
	username = StringField('Username',[validators.Length(min=4,max=15)])
	email = StringField('Email',[validators.Length(min=6,max=50)])
	password = PasswordField('New Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Passwords must match')
	])
	confirm = PasswordField('Repeat Password')