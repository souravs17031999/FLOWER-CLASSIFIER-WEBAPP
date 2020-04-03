from flask import Flask, render_template, request
from inference import get_flower_name
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def hello_world():
	if request.method == 'GET':
		return render_template('index.html',name = "sourav")
	if request.method == 'POST':
		print(request.files)
		if 'file' not in request.files:
			print('file not uploaded , please try again')
			return
		file = request.files['file']
		image = file.read()
		category,flower_name = get_flower_name(image_bytes=image)
		return render_template('result.html',flower = flower_name, category = category)
