import mysql.connector
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql@vivo", 
        database="visitor_db",
        port=3307 
    );
