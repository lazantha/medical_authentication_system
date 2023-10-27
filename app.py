from flask import Flask,render_template,redirect,flash
from models import db
import hashlib
from forms import *
from models import *
from flask_migrate import Migrate
app = Flask(__name__)
mirgrate=Migrate(app,db)

app.config['SECRET_KEY']="kEY"
# pdfkit_config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
# app.config['PDFKIT_CONFIG'] = pdfkit_config
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# bcrypt=Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/medical_database'




db.init_app(app)  # Initialize the SQLAlchemy app




#...............................................................
#error handling 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404
#error handling 500
def internal_server_error(e):
  return render_template('errors/500.html'), 500
#...............................................................


#..............................................................................
#about page
@app.route('/about')
def about():
    return render_template('about.html')
#contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')
#..............................................................................




#password encryption method
def setHash(password):

	template=hashlib.new('SHA256')
	template.update(password.encode())
	hashed_password=template.hexdigest()
	return hashed_password


@app.route('/')
def home():

    return render_template('index.html')


# .................................................

@app.route('/adminlog', methods=['POST', 'GET'])
def adminlog():
    form = AdminLog()
    if form.validate_on_submit():  # 'vallidate_on_submit' corrected to 'validate_on_submit'
        user_name = form.user_name.data
        password = form.password.data
        possition = form.possition.data  # Corrected the spelling of 'admin_type'
        department = form.department.data
        

    return render_template('logins/admin.html', form=form)






@app.route('/userlog')
def userlog():

    return render_template('logins/user.html')

# .................................................




@app.route('/adminSign', methods=['POST', 'GET'])
def adminSign():
    result=Departments.query.with_entities(Departments.calling_name).all()
    print(result)
    form = AdminSignUp()
    form.department.choices=result
    
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        gender = form.gender.data  # Corrected the data attribute
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        admin_type = form.admin_type.data  # Corrected the spelling of 'admin_type'
        department = form.department.data



    return render_template('sign/admin.html', form=form)



@app.route('/userSign')
def userSign():

    return render_template('sign/user.html')









if __name__=='__main__':
    app.run(debug=True)

