## KIDNEY DISEASE CLASSIFICATION BASED ON X-RAY IMAGES

### Problem Statement
Kidney diseases affect 850 million people globally, with CKD projected to become the 5th leading cause of death by 2040. Early detection is vital to prevent severe complications like ESRD, which requires costly treatments.

Traditional diagnostic methods are slow, expensive, and often inaccessible in resource-limited areas, leading to delayed diagnoses. Annually, 1.7 million deaths result from AKI, highlighting the urgent need for efficient solutions.

This project aims to develop a Deep Learning-based system to analyze X-ray images and detect kidney conditions like tumors, cysts, and stones, improving diagnostic speed, accuracy, and accessibility.


[Data Source](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone)
The dataset was collected from PACS in various hospitals in Dhaka, Bangladesh, featuring patients diagnosed with kidney tumors, cysts, stones, or normal findings.

Dataset contains 12,446 unique data within it in which the kidneys have:-
* **Cyst** contains 3,709,
* **Stone** 1,377, and
* **Tumor** 2,283
* and 5,077 images where the kidneys are **Normal** 

These images are in the form of X-Rays images and are passed through model's architecture where multiple features are extracted for it's disease identification.


## Dependencies
**Tech Stack** - ResNet, Tensorflow, Keras, Transfer Learning, Supervised Learning, MLFlow, DVC, and AWS.

## Project Workflow

* Designed an end to end project for identification of kidney diseases such as stone, tumour and cyst of patients based on the X-RAY images.
* Experimented with **VGGNet**, **Resnet** models for classification and fine-tuned hyperparameters to optimize their performance.
* Implemented a DVC pipeline to automate the entire process and integrated MLFlow for tracking of hyper-parameters to get the highest accuracy.
* The **config.yaml** and **params.yaml** files contain the configurations for all the processes of the entire end to end project pipeline.
* The Entity object is loaded with the required sections of these configurations.
* The Configuration manager in src config file handles the above created entity objects and makes them accessible throughout the scope of the projects based on their requirement.
* The Components specify the various functionalities of the components such as data ingestion, base model preparation, model training and mlflow metrics tracking and model evaluation.
* The Pipeline objects are responsible for creation of config objects and executing the required components' functionality as a part of the entire pipeline.
* The **main.py** file executes the entire pipeline from start to end.
* The **dvc.yaml** file includes the entire commands for executing the entire pipeline without running the previously executed commands.
* Designed a Flask UI for easy and intuitive access to the user for uploading and diagnosing their X-Ray image.


## Usage
* Access the AWS link.
* Upload the X-Ray image and hit the predict button.
* Acquire the prediction.


## Results
The model was able to process the uploaded X-Ray image and predict the disease with an accuracy of 94 %.


## Final Notes
This is a great project to learn:-
* Image processing.
* Designing and building a scalable industry grade project with a modular project structure.
* Transfer learning with multiple models such as Resnet and VGGNet and their respective architectures.
* How to use the Colab and the Kaggle environments for training such computationally expensive models.
* The working knowledge of the Tensorflow and Keras packages (model creation, callbacks designing, ).
* MLFlow tool to for tracking various configurations and choosing the best ones with best accuracy metrics.
* DVC commands for automating the entire flow.
* AWS and Docker for deployment of the project.

