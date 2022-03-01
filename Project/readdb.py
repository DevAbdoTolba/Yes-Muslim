def addStudent(con ,name, city):
    try:
        con.execute(f"""insert into count(name, city)
                    values ('{name}','{city}')""")

        con.commit()
        return True
    except:
        return False

def readStudent(con):
    data = con.execute("select * from count;")
    return data.fetchall()
