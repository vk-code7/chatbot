import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="vish1009",
  database = "chatbot"
) 
# preparing a cursor object
cursorObject = dataBase.cursor()
def addQuestion(question= ''):
    query = f"INSERT INTO chatbotdata VALUES('{question}','')"
    try:
      cursorObject.execute(query)
      print(f"{question} added to the database")
    except Exception as e:
       print('error...')
    
addQuestion("what is fees of bca")
# disconnecting from server
dataBase.close()