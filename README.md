## KIDNEY DISEASE CLASSIFICATION BASED ON X-RAY IMAGES

#### Problem Statement
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


#### Dependencies
**Tech Stack** - ResNet, Tensorflow, Keras, Transfer Learning, Supervised Learning, MLFlow, DVC, and AWS.

#### Project Workflow

* **Developed an end-to-end project** for identifying kidney diseases, including stones, tumors, and cysts, using patients' X-ray images.
* **Experimented with advanced CNN architectures** like VGGNet and ResNet, fine-tuning hyperparameters to enhance classification performance.
* **Implemented a DVC pipeline** to automate the workflow, integrating MLFlow for tracking hyperparameters and achieving optimal accuracy.
* Organized configurations in **config.yaml** and **params.yaml** files, detailing settings for the entire project pipeline.
* **Entity objects** were created to load relevant configuration sections for modular and reusable code design.
* A **Configuration Manager** in the `src.config` module handles entity objects, ensuring configurations are accessible across the project.
* Defined **components** for key functionalities, including data ingestion, base model preparation, model training, metrics tracking, and evaluation.
* Built **pipeline** objects to manage configuration creation and execute the respective components as part of the project pipeline.
* The **main.py** file integrates and executes the entire pipeline from start to finish.
* The **dvc.yaml** file automates pipeline execution, skipping previously completed steps to save time and resources.
* Designed an intuitive **Flask UI** to allow users to upload X-ray images and receive diagnostic results efficiently.


#### Deployment
* Implemented automated CI/CD pipelines using GitHub Actions by configuring AWS credentials in GitHub Secrets.
* Provisioned an EC2 instance with AmazonEC2ContainerRegistryFullAccess and AmazonEC2FullAccess policies.
* Built and pushed a Docker image to AWS ECR and deployed it on the EC2 instance.


#### Results
The model was able to process the uploaded X-Ray image and predict the disease with an accuracy of 94 %.


#### Final Notes
This is a great project to learn:-
* Image processing.
* Designing and building a scalable industry grade project with a modular project structure.
* Transfer learning with multiple models such as Resnet and VGGNet and their respective architectures.
* How to use the Colab and the Kaggle environments for training such computationally expensive models.
* The working knowledge of the Tensorflow and Keras packages (model creation, callbacks designing, ).
* MLFlow tool to for tracking various configurations and choosing the best ones with best accuracy metrics.
* DVC commands for automating the entire flow.
* AWS and Docker for deployment of the project.

