# Movie Saliency Detection Program

This program detect "saliency" of the input video. This word "saliency" means the objects that stands out in the video.
I employed old saliency detection model (not deep learning), because it is first time for me to detect salieny of video.

# Input/Output Date
・input  : movie(.mp4)  
・output : movie with saliency(.mp4) 

# Employed Salieny Detection Model
[1] StaticSaliencySpectralResidual  
https://docs.opencv.org/3.4/df/d37/classcv_1_1saliency_1_1StaticSaliencySpectralResidual.html  
[2] StaticSaliencyFineGrained  
https://docs.opencv.org/3.4/da/dd0/classcv_1_1saliency_1_1StaticSaliencyFineGrained.html

# Result 

model[1]による検出結果.  

![saliency](https://user-images.githubusercontent.com/27540739/114218629-9fd2a300-99a4-11eb-9f6b-2d95beb56c18.gif)

Video by Coverr-Free-Footage from Pixabay
https://pixabay.com/ja/videos/カメラマン-ビーチ-写真-91/
