# FLOWER-CLASSIFIER-WEBAPP
This is an neural network webapp visualizing the training of the network and testing accuracy of 98.6% accuracy.
The neural network uses pretrained resnet152 and then trained to classify images of flowers.
It is built using Pytorch framework using Python as primary language.
The webapp is built using flask.

## Dataset used :     
102 Category Flower Dataset     

http://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html     
[Maria-Elena Nilsback](http://www.robots.ox.ac.uk/~men/) and [Andrew Zisserman](http://www.robots.ox.ac.uk/~az/)

## Neural Network used : 
[Resnet152](https://resources.wolframcloud.com/NeuralNetRepository/resources/ResNet-152-Trained-on-ImageNet-Competition-Data)    
[Network Layers in Pytorch](https://github.com/pytorch/vision/blob/master/torchvision/models/resnet.py)     


## Run on windows - 
Make sure you have installed Python , Pytorch and flask.

* _First download all the folders and files_     
`git clone https://github.com/souravs17031999/FLOWER-CLASSIFIER-WEBAPP.git`     
* _Then open the command prompt (or powershell) and change the directory to the path where all the files are located._       
`cd FLOWER-CLASSIFIER-WEBAPP`      
* _Now run the following commands_ -        

`set FLASK_APP=flower.py`   

`python -m flask run`      


This will firstly download the models and then start the local web server.

now go to the local server something like this - http://127.0.0.1:5000/ and see the result and explore.

@creator - sourav kumar
