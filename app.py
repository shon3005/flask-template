from flask import Flask, render_template, request
import os
import datetime
from syncano import client
SyncanoApi = client.SyncanoApi
app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
	if request.headers.getlist("X-Forwarded-For"):
   		ip = request.headers.getlist("X-Forwarded-For")[0]
	elif request.access_route:
		ip = request.access_route
	else:
   		ip = request.remote_addr
	syncano = SyncanoApi("cold-dew-135677","c418ff4e58fb13638c549b41300a918fc60aa84e")
	project_id = "5941"
	collection_id = "18472"
	syncano.data_new(project_id,collection_id=collection_id,title=ip,text=str(datatime.datetime.now()))
	return render_template("index.html")


if __name__ == '__main__':
	app.run(debug=True)
