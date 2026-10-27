import mysql.connector


mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kmg web"
    
)

mycursor = mydb.cursor()
sql ="INSERT INTO admin(name,contact,address) VALUES (%s,%s,%s)"
val = ("gowtham","9585636959","coimbatore")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"details collected.")