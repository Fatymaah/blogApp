from flask import (Flask, render_template, request, make_response)
import json
import models
from models.models import Myentry



app = Flask('app')


@app.route('/')
def index():
  
  return render_template("index.html",)


@app.route('/add', methods=['POST','GET'])
def add():
  data = dict(request.form.items())
  if data.get('title',None):
    Myentry.create(
      title = data.get('title','Birthday'),
      body = data.get ('body','Multiple lines of text that form the lede, informing new readers quickly and efficiently about  contents.'),
      created_at = data.get('created_at',2018-7-1),
      
     
    )
  return render_template("add.html")
    
@app.route('/blogs')
def blogs():
    models.models.initialize()
    blogs = models.models.Myentry.select()
    return render_template("list_entry.html", blogs = blogs)

  

app.run(debug=True, host='0.0.0.0', port=8080)