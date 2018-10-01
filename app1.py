from flask import Flask, render_template, json, request


app = Flask(__name__)

# def dbConfig():
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
mysql = MySQL()




@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

# @app.route('/signUp')
# def signUp():


# @app.route('/signUp',methods=['POST'])
# def signUp():



@app.route('/signUp',methods=['POST'])
def signUp():
	#read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
 
    # validate the received values
    if _name and _email and _password:
    	# dbConfig()
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})



if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')

