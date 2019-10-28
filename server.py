from flask import Flask, request, render_template, session
from flaskext.mysql import MySQL
# import MySQLdb
import mysql.connector


app = Flask(__name__)

# app.config['MYSQL_DATABASE_HOST']='localhost'
# app.config['MYSQL_DATABASE_USER']='root'
# app.config['MYSQL_DATABASE_PASSWORD']=''
# app.config['MYSQL_DATABASE_HOST']='mydb'

# mysql.init_app(app)
mydb = mysql.connector.connect(
    host="localhost",
    user="neelima",
    passwd="neelima123",
    database="stocks",
    buffered=True
)
mycursor = mydb.cursor(buffered=True)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')



@app.route("/login")
def login():
    try:   
        mySql = "select * from login WHERE username ='amitha'"
        mycursor.execute(mySql)
        mydb.commit()
        data1 = mycursor.fetchall()
        if len(data1) > 0:
            # session['username']= username
            return render_template('admin_home_page.html', username=session['username'])
        else:
            return render_template('login.html')
    except Exception as e:
        return(str(e))
    # username =request.form['username']
    # password =request.form['password']

    # if request.method=='GET':
    #     username=request.args.get('username')
    #     password=request.args.get('password')

    #     cursor.execute("select * from login where username='"+username+"' and password='"+password+"'")
    #     data1=cursor.fetchall()
    #     if len(data1)>0:
    #         session['username']=username
    #         return render_template('admin_home_page.html',username=session['username'])
    #         else:

    return render_template('login.html')




@app.route("/admin")
def admin():
    return render_template('admin_home_page.html')
    
@app.route("/forgot")
def forgot():
    return render_template('forgot_password.html')


@app.route("/stockin")
def stockin():
    return render_template('stock_inventory.html')


@app.route("/addstock")
def addstock():
    return render_template('add_stock.html')


@app.route("/move")
def move():
    return render_template('move.html')


@app.route("/report")
def report():
    return render_template('report.html')


@app.route("/guest")
def guest():
    return render_template('guest_home.html')


if __name__ == '__main__':
    app.route(debug=True)
