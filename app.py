# Name:Sarthak Kapaliya
# Date:24/7/2022

from flask import Flask, render_template, request
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
app = Flask(__name__)

dic = {0 : 'Auto', 1 : 'Bus', 2 : 'Car', 3 : 'Tempo', 4 : 'Tractor', 5 : 'Truck'}

model = load_model('Models/Vehicle_aug1.h5')
model.make_predict_function()
def realpredict_fuction(img_path):
    i = tf.keras.utils.load_img(img_path, target_size=(100,100))
    i= tf.keras.utils.img_to_array(i)/255.0
    i = i.reshape(1, 100,100,3)
    y_pred = model.predict(i)
    y_pred = y_pred > 0.5
    y_pred
    list_pred = y_pred.tolist()
    list1 = list_pred[0]
    if list1[0] == True:
        return "Auto"
    elif list1[1] == True:
        return "Bus"
    elif list1[2] == True:
        return "Car"
    elif list1[3] == True:
        return "Tempo"
    elif list1[4] == True:
        return "Tractor"
    elif list1[5] == True:
        return "Truck"
    else:
        return "Don't Know"
# routes
@app.route("/")
def main():
	return render_template("home.html")

@app.route("/templates/index", methods=['GET', 'POST'])
def index():
	return render_template("index.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "F:/IMP DOCUMENT/projects/ISRO/SCL-MEITy-Project-2022/static/" + img.filename	
		img.save(img_path)

		p = realpredict_fuction(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)

if __name__ =='__main__':
	app.run(debug = True)