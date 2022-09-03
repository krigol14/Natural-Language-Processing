from mysql.connector import connection
import nltk
import mysql.connector
from nltk import load_parser

# load the grammar and vocabulary we have created in the 'grammar_vocabulary.fcfg' file
grammar = nltk.data.load('grammar_vocabulary.fcfg') 
# allows us to read the grammar into NLTK, ready for use in parsing
chart_parser = load_parser('grammar_vocabulary.fcfg')     

# natural language query entered by the user
# example queries shown below
'''
nl_query = "who has food"
nl_query = "who loves book"
nl_query = "who runs quickly"
nl_query = "who chases cat"
'''
nl_query = "who needs food"

# using the .fcfg file we created and the user's query, 
# create an SQL query in order to submit it to the database and get the wanted answer
# split the nl_query into tokens
tokens = nl_query.split()               
# parse the tokens using the chart parser we created earlier
parsed = chart_parser.parse(tokens)      
trees = list(parsed)            

query = trees[0].label()['SEM']
query = [i for i in query if i]
# final form of the query that will be submitted to the database
query_db = ' '.join(query) + ';'       

# establish connection with the database 'nlp_db' giving our credentials
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "test123",
    database = "nlp_db"
)

# create a cursor object in order to submit the query created to the database
cursor = connection.cursor()
# execute the query
cursor.execute(query_db)
# fetch the answers from the database
records = cursor.fetchall()
for row in records:
    print("Your question: " + nl_query)
    print(query_db)
    print("The answer to your question is: " + row[0])

connection.close()
