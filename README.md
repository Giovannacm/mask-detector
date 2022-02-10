# mask-detector
FPGA course assignment

# Introduction
Computer Vision tools have been applied in several areas, such as agriculture, surveillance, automobile industry, and others. Due to the pandemic caused by the coronavirus, monitoring people wearing a mask in public and private environments is essential for everyone's safety, even after the advancement of vaccination. The development of an algorithm for this purpose on architectures like the Raspberry Pi allows a more accessible use of this system. In this sense, the project's main objective is to develop a masked face recognition system using the Raspberry Pi microprocessor, a camera module for this computer, the Python programming language and several libraries available for this language.

# Materials and Methods
The materials used in this project were: Raspberry Pi 3 - model B, Raspberry Pi Camera Module V2, Python programming language and libraries available for this language (OpenCV, sklearn, keras, tensorflow, etc). The project starts with the pre-processing of a dataset acquired over the Internet. This dataset is composed of faces with masks, without masks and using them inappropriately. The pre-processed data were used in the training and testing of the classifiers. Regarding the classifiers, two examples available in the literature (DT and KNN) and a neural network were evaluated. Among the three models created, only one was selected for the classification of the image acquired in real time by the camera module.
