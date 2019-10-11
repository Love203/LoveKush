from flask import Flask,render_template,url_for,request,flash,redirect

from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
cluster = Cluster('couchbase://localhost:8091')
authenticator = PasswordAuthenticator('lovekush', '123456')
cluster.authenticate(authenticator)
cb = cluster.open_bucket('MyBucket')
app = Flask(__name__,template_folder='template')

@app.route("/")
def index():

    
    cb.upsert('12', {'DockingID': 'D1', 'ClientName':'Pearson',
                     'ClientID':'Pearson101','CustomerName':'Amol Borse','CustomerID':'Amol111','Expression':'Smile','Probability':8.6,'DateTime': '2019-10-03T15:10:05.999'})
    cb.upsert('13', {'DockingID': 'D2', 'ClientName':'IBM',
                     'ClientID':'IBM102','CustomerName':'Lovekush','CustomerID':'Sham112','Expression':'Sad','Probability':8.7,'DateTime': '2019-10-03T15:10:05.99'})
    cb.upsert('14', {'DockingID': 'D3', 'ClientName':'Vertica',
                     'ClientID':'Vertica103','CustomerName':'Ajay Rathod','CustomerID':'Ajay113','Expression':'Smile','Probability':8.0,'DateTime': '2019-10-03T15:10:05.99'})
    cb.upsert('15', {'DockingID': 'D4', 'ClientName':'Tata',
                     'ClientID':'Tata104','CustomerName':'Ratan Tata','CustomerID':'Ratan113','Expression':'Smile','Probability':8.2,'DateTime': '2019-10-03T15:10:05.99'})
  
# OperationResult<RC=0x0, Key=u'u:king_arthur', CAS=0xb1da029b0000>
   
    
# {u'interests': [u'Holy Grail', u'African Swallows'], u'name': u'Arthur', u'email': u'kingarthur@couchbase.com'}
## The CREATE PRIMARY INDEX step is only needed the first time you run this script
    from couchbase.n1ql import N1QLQuery
    row_iter = cb.n1ql_query(N1QLQuery('SELECT DockingID,ClientName,ClientID,CustomerName,CustomerID,Expression,Probability,DateTime FROM MyBucket' ))
    l=[]
    for row in row_iter:
        l.append(row)
    print(l)
    return render_template('index.html',result=l)
	
@app.route("/test" , methods=['GET','POST'])
def test():
    select = request.values.get('comp_select')
    var=str(select)
    
    from couchbase.n1ql import N1QLQuery
    row_iter = cb.n1ql_query(N1QLQuery('SELECT DockingID,ClientName,ClientID,CustomerName,CustomerID,Expression,Probability,DateTime FROM MyBucket' ))
    l=[] 
    for row in row_iter:
        l.append(row)
    return  render_template('index.html',result=l,r=var)
	

if __name__ == "__main__":
	app.run(debug=True)
    

