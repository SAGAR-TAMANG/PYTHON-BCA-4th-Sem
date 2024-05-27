import mysql.connector

try:
  connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='new'
  )

  if connection.is_connected():
    print("Connection Established")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM mytable")
  else:
    print("Connection not done")

except Exception as e:
  print("MYSQL Connector Finish: ", e)