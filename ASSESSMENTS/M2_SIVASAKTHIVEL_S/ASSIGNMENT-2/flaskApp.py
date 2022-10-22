from flask import Flask,render_template,request,url_for 
from flask_mysqldb import MySQL 
app=Flask(__name__) 
app.config['MYSQL_HOST']='localhost' 
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flask_application' 
mysql=MySQL(app)
@app.route("/") 
def home(): 
    cur=mysql.connection.cursor() 
    cur.execute("SELECT * FROM signup") 
    fetchdata=cur.fetchall() 
    return render_template("home.html",datas=fetchdata)
@app.route("/signin",methods=['GET','POST']) 
def signin():  
    if request.method=='POST': 
        email=request.form['mailid'] 
        pswd=request.form['pswd'] 
        cur=mysql.connection.cursor() 
        cur.execute('SELECT * FROM signup') 
        fetchdata=cur.fetchall() 
        for data in fetchdata: 
            if(data[4]==email and data[5]==pswd): 
                return render_template("home.html",datas=fetchdata)
    return render_template("signin.html")
@app.route("/signup",methods=['GET','POST']) 
def signup():
    if request.method=='POST': 
        fname=request.form['firstname'] 
        lname=request.form['lastname'] 
        contact=request.form['contactno'] 
        mailid=request.form['mailid'] 
        pswd=request.form['pswd'] 
        cur=mysql.connection.cursor()
        sql="insert into signup(firstname,lastname,contactno,mailid,pswd) values(%s,%s,%s,%s,%s)" 
        cur.execute(sql,[fname,lname,contact,mailid,pswd])
        mysql.connection.commit()
        cur.execute('SELECT * FROM signup') 
        fetchdata=cur.fetchall() 
        cur.close() 
        return render_template("home.html",datas=fetchdata)
    return render_template("signup.html")
@app.route("/userinfo/<int:id>") 
def userinfo(id): 
    id1=id
    cur=mysql.connection.cursor() 
    cur.execute('SELECT * FROM signup where id=%s',[id1]) 
    fetchdata=cur.fetchall()
    return render_template("userinfo.html",datas=fetchdata)    
if(__name__=='__main__'):
    app.run(debug=True)