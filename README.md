# Chang-e-5-rockclassification-MRNet
A brand new CNN architecture for rock classification task detected by Chang'e 5 probe NaTeCam

Here is a CNN architecture designed for rock classification.

![image](https://user-images.githubusercontent.com/95695195/169642176-36d361c3-88d4-4df0-86e0-1e382e9b36ab.png)


It contains two data set:


1. earth rock dataset:divided into igneous, metamorphic and sedimentary.3 categories 



2.CE5ROCK:processed by skimage and partly originated from CNSA Chang'e 5 lunar rover navigation and terrain camera
I'm regret to tell you this part has not been disclosed so that it is unavailble right now(2022.5.21), but you may apply for the data on https://moon.bao.ac.cn/ce5web/moonGisMap.search

It also contains the rock image from NASA curator of the moon, divided into 3 categories: basalt(igneous), crustal(metamorphic) and breccia(sedimentary)





Before running the script you need to unzip the image data set first. Train and test set has already been divided in moderate proportion.

The ipynb script can only be executed in jupyter notebook server with GPU.
