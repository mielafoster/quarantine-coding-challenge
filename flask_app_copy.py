from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

#This is our database conenction
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'FGPV8A1K'
app.config['MYSQL_DB'] = 'oakbeta'#still need to nake this database in mysql

mysql = mySQL(app)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods = ['GET', 'POST'])
def insert():
    if request.method == "POST":
        consultation = request.form
        q1 = details['name']
        q2 = details['email']
        q3 = details['pattern']
        q4 = details['length']
        q5 = details['density']
        q6 = details['width']
        q7 = details['scalp']
        q8 = details['dandruff']
        q9 = details['color']
        q10 = details['comb']
        q11 = details['chemical']
        q12 = details['strand']
        q13 = details['shower']
        q14 = details['protective']
        q15 = details['wetfeel']
        q16 = details['elastic']
        q17 = details['break']
        q18 = details['detangle']
        q19 = details['split']
        q20 = details['knots']
        q21 = details['style']
        q22 = details['shampoo']
        q23 = details['condition']
        q24 = details['trim']
        q25 = details['heat']
        q26 = details['manipulate']
        q27 = details['protective_styles']
        q28 = details['activities']
        q29 = details['zipcode']
        q30 = details['age']
        q31 = details['allergies']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO  oakbeta(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('display.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug= True)
