import pymongo
from flask import Flask , request , jsonify
from flask import jsonify

app=Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.qp51p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db=client.kumarmongo

def show_database():
	x=client.list_database_names()
	print(x)

def create_collection():
	global col1
	col1=db['student_data2']

def insert_data():
	dict={
	    'name': 'Chandrakanta',
	    'email_id': 'chakara@gmail.com',
	    'product': 'chakaraAi',
	    'company': 'Chakru'
	}
	col1.insert_one(dict)

@app.route('/fetch',methods=['POST'])
def fetch():
	if request.method=='POST':
		c=col1.find()
		data=[]
		for i in c:
			data.append(i)
	return jsonify(str(data))

if __name__ == '__main__':
	create_collection()
	insert_data()
	app.run()
