from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class SignupForm(FlaskForm):
    name        = StringField('Nombre', validators=[DataRequired(message='Campo requerido'), Length(min=5,max=20,message='Máximo 20 caractéres')])
    password    = PasswordField('Password', validators=[DataRequired(message='Campo requerido'), EqualTo('confirm', message='No coninciden')])
    confirm     = PasswordField('Repite la contraseña')
    email       = StringField('Email',validators=[DataRequired(message='Campo requerido'), Email()])
    submit      = SubmitField('Registrar')

class PostForm(FlaskForm):
    title       = StringField('Titulo', validators=[DataRequired(message='Campo obligatorio'), Length(max=50)])
    title_slug  = StringField('Titulo Slug', validators=[DataRequired(message='Campo obligatorio'), Length(max=128)])
    content     = TextAreaField('Contenido', validators=[DataRequired(message='Campo Obligatorio'), Length(max=400)])
    submit      = SubmitField('Enviar')