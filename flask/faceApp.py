# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 00:36:56 2019

@author: lovekush.chaurasia
"""

from flask import Flask,render_template,url_for,flash,redirect
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request

app = Flask(__name__,template_folder='template')

'''app.config["MONGO_DBNAME"]= "myMongoDB"'''
app.config['MONGO_URI'] ="mongodb+srv://lovekush:lovekush@cluster1-cuqsq.mongodb.net/myMongoDB?retryWrites=true&w=majority"

mongo = PyMongo(app)

'''@app.route("/")
def index():

    
    mongo.db.user.insert({'DockingID': 'D1', 'ClientName':'Pearson',
                     'ClientID':'Pearson101','CustomerName':'Amol Borse','CustomerID':'Amol111','Expression':'Smile','Probability':8.6,'DateTime': '2019-10-03T15:10:05.999'})
    mongo.db.user.insert({'DockingID': 'D2', 'ClientName':'IBM',
                     'ClientID':'IBM102','CustomerName':'Lovekush','CustomerID':'Sham112','Expression':'Sad','Probability':8.7,'DateTime': '2019-10-03T15:10:05.99'})
    mongo.db.user.insert({'DockingID': 'D3', 'ClientName':'Vertica',
                     'ClientID':'Vertica103','CustomerName':'Ajay Rathod','CustomerID':'Ajay113','Expression':'Smile','Probability':8.0,'DateTime': '2019-10-03T15:10:05.99'})
    mongo.db.user.insert({'DockingID': 'D4', 'ClientName':'Tata',
                     'ClientID':'Tata104','CustomerName':'Ratan Tata','CustomerID':'Ratan113','Expression':'Smile','Probability':8.2,'DateTime': '2019-10-03T15:10:05.99'})
    return '<h1>Added a user!</h1>'



    row_iter = mongo.db.user.find()
    l=[]
    for row in row_iter:
        l.append(row)
    print(l)
    return render_template('index.html',result=l)'''

	
@app.route("/test" , methods=['GET','POST'])
def test():
    select = request.values.get('comp_select')
    var=str(select)
    row_iter = mongo.db.user.find()
    l=[]
    for row in row_iter:
        l.append(row)
    print(l)
    return  render_template('index.html',result=l,r=var)

@app.route('/a')
def indexx():
    return render_template('frm.html')

@app.route('/create', methods=['POST'])
def create():
     
    if 'img' in request.files:
        profile_image = request.files['img']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.user1.insert({'ClientName' : request.form.get('ClientName'),'CustomerName' : request.form.get('cn'),'date' : request.form.get('date'), 'profile_image_name' :profile_image.filename})
    
    return 'Done!'

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

@app.route('/profile/<CustomerName>')
def profile(CustomerName):
    user = mongo.db.user1.find_one_or_404({'CustomerName' : CustomerName})
    return f'''
        <h1>{CustomerName}</h1>
        <img src = "{url_for('file', filename=user['profile_image_name'])}">
    '''
      

	

if __name__ == "__main__":
    app.run(debug=False)