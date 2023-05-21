import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="vish1009",
  database = "chatbot"
)
#print(dataBase)
db = dataBase.cursor()

# preparing a cursor object
cursorObject = dataBase.cursor()

# disconnecting from server
def getResponse(Question) :
    query = f"SELECT response FROM chatbotdata Where question = '{Question}'"
    cursorObject.execute(query)
    result = cursorObject.fetchall()
    return result[0][0]

#print(getResponse("what can you do"))
