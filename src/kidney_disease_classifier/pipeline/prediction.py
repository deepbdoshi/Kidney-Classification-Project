import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename

    
    def predict(self):
        # load model
        model = load_model("data\training\final_model.h5")

        imagepath = self.filename
        loaded_image = image.load_img(imagepath, target_size = (224,224))
        loaded_image = image.img_to_array(loaded_image)
        loaded_image = np.expand_dims(loaded_image, axis = 0)
        result = np.argmax(model.predict(loaded_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Cyst'
            return [{ "image" : prediction}]
        if result[0] == 2:
            prediction = 'Normal'
            return [{ "image" : prediction}]
        if result[0] == 3:
            prediction = 'Stone'
            return [{ "image" : prediction}]
        else:
            prediction = 'Tumor'
            return [{ "image" : prediction}]