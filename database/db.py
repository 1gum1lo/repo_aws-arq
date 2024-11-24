import pymysql

db_host = 'database-1.cpia0k4iiqev.us-east-2.rds.amazonaws.com'
db_user= 'admin'
db_psw = 'admin-123'

try:
    connection_db = pymysql.connect(
        host = db_host,
        user = db_user,
        password = db_psw 
    )

    print("Conexión exitosa a la DB")
except Exception as err:
    print("Error: ", err)
    connection_db = None

def add_user(id, nombre, apellido, nacimiento):
    
    instruction_sql = "INSERT INTO db_users.users(id, nombre, apellido, nacimiento) VALUES ("+id+" , '"+nombre+"', '"+apellido+"','"+nacimiento+"')"
    #print(connection_db)
    try:
        cursor = connection_db.cursor()
        cursor.execute(instruction_sql)
        connection_db.commit()
        print("Usuario Registrado")
    except Exception as err:
        print("Error:", err)

def consult_user(id):
    
    instruction_sql = "SELECT * FROM db_users.users WHERE id="+id
    #print(connection_db)
    try:
        cursor = connection_db.cursor()
        cursor.execute(instruction_sql)
        result = cursor.fetchall()
        print("Usuario Consultado")
        return result
    except Exception as err:
        print("Error:", err)
