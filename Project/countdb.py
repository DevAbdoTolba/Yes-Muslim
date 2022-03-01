
import sqlite3 

#create database
con = sqlite3.connect("count.db")  
cursor = con.cursor()
print("Database opened successfully")
#create table  
con.execute("""create table Count
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        City TEXT NOT NULL,
        Count int NOT NULL)""")  
print("Table created successfully")  

sql2 = """INSERT INTO Count('id','City','Count') VALUES ('1','Cairo','0'),('2','Alexandria','0'),('3','Aswan','0'),('4','Beheira','0'),('5','Beni Suef','0'),('6','Luxor','0'),('7','Dakahlia','0'),('8','Fayoum','0'),('9','Gharbia','0'),('10','Giza','0'),('11','Ismailia','0'),('12','Kafr el-Sheikh','0'),('13','Matrouh','0'),('14','Minya','0'),('15','Menofia','0'),('16','New Valley','0'),('17','North Sinai','0'),('18','Port Said','0'),('19','Qualyubia','0'),('20','Qena','0'),('21','Red Sea','0'),('22','Al-Sharqia','0'),('23','Sohag','0'),('24','South Sinai','0'),('25','Suez','0')"""
cursor.execute(sql2)
con.commit()
con.close()


