from unicodedata import name
from flask import Flask, redirect, request, session, url_for,render_template
import sqlite3
from pickle import NONE
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    page = """<!DOCTYPE html>
            <html>
            <head>
            <title><(&nbsp;&nbsp;&nbsp;  &#9862; &#9862;)> Info page</title>
                <button><a href="login">Login</a></button>
                <!-- <button><a href="allCities">Scores</a></button> -->
            </head>
            <body style="background-color:#0099ff;">

            <p><font size="+6" style="color:white"><center><hr><a href="https://justpaste.it/94cp2" style="color:white"><u>Yes...&nbsp;&nbsp;<a href="https://justpaste.it/99oop" style="color:white"> Muslim</a></u></a></font></p>
            <p><center><p><font size="+3">
                This web is meant to be made to compete Egyptians in an Islamic competition
                inspired by a pop cat!</font></p><br><p><font size="+3">we show the most clicked cities in the count of praises clicked on,
                that is pretty much it!</font></p><br> <p><font size="+3">thanks for reading :D
                click on <a href="login">>me</a> to login and start competing</font></p>.<br><br><br>
                <img src="https://i.ibb.co/z8BXbG5/pngtree-holy-quran-icon-design-vector-png-image-1585279.png">
            
            
            </body>
            </html> """
    return page


@app.route('/login', methods=["GET","POST"]) 
def login():
    if request.method == "GET":
        page = """
        <!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>login form</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
<link href="../static/css/css.css" rel="stylesheet" type="text/css">
  </head>

  <body>
  <br>
  <br>
  <br>
  <br>
  <br><center>
    <form action="" method="post">
      <input type="text" name="name" placeholder="name">
      <label for="city" placeholder="city"></label>

            <select id="city" name="city" placeholder="city">
                <option value="Cairo">Cairo</option>
                <option value="Alexandria">Alexandria</option>
                <option value="Aswan">Aswan</option>
                <option value="Beheira">Beheira</option>
                <option value="Beni Suef">Beni Suef</option>
                <option value="Luxor">Luxor</option>
                <option value="Dakahlia">Dakahlia</option>
                <option value="Tanta">Tanta</option>
                <option value="Damietta">Damietta</option>
                <option value="Fayoum">Fayoum</option>
                <option value="Gharbia">Gharbia</option>
                <option value="Giza">Giza</option>
                <option value="Ismailia">Ismailia</option>
                <option value="Kafr el-Sheikh">Kafr el-Sheikh</option>
                <option value="Matrouh">Matrouh</option>
                <option value="Minya">Minya</option>
                <option value="Menofia">Menofia</option>
                <option value="New Valley">New Valley</option>
                <option value="North Sinai">North Sinai</option>
                <option value="Port Said">Port Said</option>
                <option value="Qualyubia">Qualyubia</option>
                <option value="Qena">Qena</option>
                <option value="Red Sea">Red Sea</option>
                <option value="Al-Sharqia">Al-Sharqia</option>
                <option value="Sohag">Sohag</option>
                <option value="South Sinai">South Sinai</option>
                <option value="Suez">Suez</option>
            </select>
            <input type="submit" value="Submit">

    </form>
  </body>
</html>

            """
        return page
    elif request.method=="POST":

        name = request.form['name']
        city = request.form['city']
        # connect to DB
        con = sqlite3.connect('count.db')        
        con.close()        
        page = f" Hello {name}<br> Your city: {city}"  

        link = "<br><a href='clicker'>Go to clicker!</a>"

        session['City']=city
        session['Name']=name
        
        return redirect(url_for('clicker'))
        
def AllTablesInfo(cursor):
    TableNameWithColumnInfo=[]
    AllTablesNames=[]
    cursor= cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for TableInfo in cursor.fetchall():
        for EachTable in TableInfo:
            AllTablesNames.append(EachTable)
            cursor=cursor.execute(f"PRAGMA table_info({EachTable})")
            ColumnNameWithDataType=[]
            for ColumnInfo in cursor.fetchall(): 
                ColumnNameWithDataType.append([ColumnInfo[1],ColumnInfo[2]])
            TableNameWithColumnInfo.append([EachTable,ColumnNameWithDataType])
    return TableNameWithColumnInfo,AllTablesNames

@app.route("/allCities")
def allCities():
    con = DbConnection()
    cursor = sqlite3.Cursor(con)
    TablesInfo,AllTablesName = AllTablesInfo(cursor)
    TableData=[]

    for names in TablesInfo:
            if names[0] == 'Count':                     
                    cursor = con.execute(f"SELECT * FROM Count")
                    for Col in cursor.fetchall():  
                        TemporaryDictionary={}
                        for ColumnIndex in range(0,len(names[1])):
                            TemporaryDictionary[names[1][ColumnIndex][0]]=Col[ColumnIndex]
                        TableData.append(TemporaryDictionary)

    print(TableData)

    return render_template('allCities.html',TableData=TableData)
#def newCity:
    








def DbConnection():
    con = NONE
    try:
        con=sqlite3.connect("count.db")
    except sqlite3.Error as e:
        print(e)
    return con


@app.route('/clicker',methods = ["POST","GET"])    
def clicker():
    con = DbConnection()
    cursor = sqlite3.Cursor(con)
    name = session.get('Name',None)
    print(session.get('Name',None))
    print(session.get('City',None))
    

    clicks1=0
    clicks2=0
    clicks3=0
    clicks4=0
    out =0

    if str(request.form.get('TextBox1')) != 'None':
        clicks1 = int(str(request.form.get('TextBox1')))
    if str(request.form.get('TextBox2')) != 'None':
        clicks2 = int(str(request.form.get('TextBox2')))
    if str(request.form.get('TextBox3')) != 'None':
        clicks3 = int(str(request.form.get('TextBox3')))
    if str(request.form.get('TextBox4')) != 'None':
        clicks4 = int(str(request.form.get('TextBox4')))
    



    
    if (clicks1+1) %33 == 0 and clicks1+1 != 0:
        Cnt = list(Col[0]   
        for Col in con.execute(f"SELECT Count from Count WHERE City = '{session.get('City',None)}'").fetchall()
        )[0]
        Cnt+=33
        out = Cnt
        
        cursor = con.execute(f"UPDATE Count SET Count = {Cnt} WHERE City =  '{session.get('City',None)}'")
        con.commit()
        print(str(session.get('City',None))+' Is now : '+str(out))

    if (clicks2+1) %33 == 0 and clicks2+1 != 0:
        Cnt2 = list(Col[0]   
        for Col in con.execute(f"SELECT Count from Count WHERE City = '{session.get('City',None)}'").fetchall()
        )[0]
        Cnt2+=33
        out = Cnt2
        cursor = con.execute(f"UPDATE Count SET Count = {Cnt2} WHERE City =  '{session.get('City',None)}'")
        con.commit()
        print(str(session.get('City',None))+' Is now : '+str(out))


    if (clicks3+1) %34 == 0 and clicks3+1 != 0:
        Cnt3 = list(Col[0]   
        for Col in con.execute(f"SELECT Count from Count WHERE City = '{session.get('City',None)}'").fetchall()
        )[0]
        Cnt3+=33
        out = Cnt3
        cursor = con.execute(f"UPDATE Count SET Count = {Cnt3} WHERE City =  '{session.get('City',None)}'")
        con.commit()
        print(str(session.get('City',None))+' Is now : '+str(out))

    if (clicks4+1) %100 == 0 and clicks4+1 !=0:
        Cnt4 = list(Col[0]   
        for Col in con.execute(f"SELECT Count from Count WHERE City = '{session.get('City',None)}'").fetchall()
        )[0]
        Cnt4+=33
        out = Cnt4
        cursor = con.execute(f"UPDATE Count SET Count = {Cnt4} WHERE City =  '{session.get('City',None)}'")
        con.commit()
        print(str(session.get('City',None))+' Is now : '+str(out))


    # if request.form.get('Submit') == "Submit":

    if request.method =='GET':
        clicks1, clicks2, clicks3, clicks4 = ZeroNumbers()
    

    if request.method =='POST':
        if request.form.get('Button1') == "سبحان الله":
            clicks1+=1
        if request.form.get('Button2') == "الحمد لله":
            clicks2+=1
        if request.form.get('Button3') == "الله أكبر":
            clicks3+=1
        if request.form.get('Button4') == "لا إله إلا الله":
            clicks4+=1
        if request.form.get('Submit1') == "Submit" :
            Submitting(con)
            clicks1, clicks2, clicks3, clicks4 = ZeroNumbers()
        if request.form.get('Submit1') == "Login" :
            Submitting(con)
            clicks1, clicks2, clicks3, clicks4 = ZeroNumbers()
            # DON'T GO BACK!! ONLY SUBMIT
            return redirect(url_for('login'))
        if request.form.get('Submit1') == "Scores" :
            Submitting(con)
            clicks1, clicks2, clicks3, clicks4 = ZeroNumbers()
            # DON'T GO BACK!! ONLY SUBMIT
            return redirect(url_for('allCities'))
        


    page = f"""
  <!DOCTYPE html>



  <html lang="en" dir="ltr">
   <head>
   <link href="../static/css/css2.css" rel="stylesheet" type="text/css">
      <form method="POST">
    <input type="Submit" name="Submit1" value="Login">
    <input type="Submit" name="Submit1" value="Scores">
    <meta charset="utf-8">
    <meta name="description" content="this is my site ">
    <title><( &nbsp;&nbsp;&nbsp; 0.0)> Clinck </title>
   </head>


   <body style="background-color:#0099ff;" >
      





    <p style="color:black; font-family"verdana" size="+6"><font size="+7"><a  href='/' >Yes &nbsp; muslim </a></font></p><br><br>



     <p> <button type="button" onclick="alert('Nice broder (✌ﾟ∀ﾟ)☞')">Muslim {name}?</button>


  


  <hr>



    <p>
   <input type="submit" class="button" name="Button1" value="سبحان الله"/>
   <input type="text"  class="text" name="TextBox1" value={clicks1} readonly="readonly" /> 33 مرة</p>
  <div>




    <p>
   <input type="submit"  class="button" name="Button2" value="الحمد لله"/> 
   <input type="text" class="text" name="TextBox2" value={clicks2} readonly="readonly" /> 33 مرة</p>
  </div>


    <p>
    <input type="submit"  class="button" name="Button3" value="الله أكبر"/>
    <input type="text" class="text" name="TextBox3" value={clicks3} readonly="readonly" /> 34 مرة</p>
   
  <div>


    <p>
    <input type="submit"  class="button" name="Button4" value="لا إله إلا الله"/> 
    <input type="text" class="text" name="TextBox4" value={clicks4} readonly="readonly" /> 100 مرة</p>
    
    
   
  <div>

<form>
    <input type="Submit" name="Submit1" value="Submit">
    
</form>

  </form>
   </body>
  </html>
  """
    



  
   


    return page

def ZeroNumbers():
    clicks1=0
    clicks2=0
    clicks3=0
    clicks4=0
    return clicks1,clicks2,clicks3,clicks4

def Submitting(con):
    Submit1 = int(request.form['TextBox1']) + int( request.form['TextBox2']) + int( request.form['TextBox3']) + int( request.form['TextBox4'])
    Submit1+=  list(Col[0]   
            for Col in con.execute(f"SELECT Count from Count WHERE City = '{str(session.get('City',None)).strip()}'").fetchall()
            )[0]
    cursor = con.execute(f"UPDATE Count SET Count = {Submit1} WHERE City =  '{session.get('City',None)}'")
    con.commit()
    print(str(session.get('City',None))+' Is now : '+str(Submit1))
    


#Errors \(;-; )/
#Back from any site(login, scores) repets submtion
#intering scores before logging in, CRASH :D
#
