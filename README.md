# FLOWER-CLASSIFIER-WEBAPP
This is an neural network webapp visualizing the training of the network and testing accuracy of 98.6% accuracy.
The neural network is pretrained on resnet152 and then trained to classify images of flowers.
It is built using Pytorch framework using Python as primary language.
The webapp is built using flask.


## Run on windows - 
Make sure you have installed Python , Pytorch and flask.

* _First download all the folders and files_
* _Then open the command prompt and change the directory to the path where all the files are located._
* _Now run the following commands -

> set FLASK_APP=flower.py

> python -m flask run

This will firstly download the models and then start the local web server.

now go to the local server something like this - http://127.0.0.1:5000/ and see the result and explore.
