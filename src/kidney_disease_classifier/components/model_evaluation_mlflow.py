from pathlib import Path
from urllib.parse import urlparse
from kidney_disease_classifier.entity.config_entity import EvaluationConfig
from kidney_disease_classifier.utils.common import read_yaml, create_directories, save_json

import tensorflow as tf
import mlflow
import mlflow.keras

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
    
    def _valid_generator(self):
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.30)

        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear")

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = "validation",
            shuffle = False,
            **dataflow_kwargs)


    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path, compile=False)

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self.model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.01),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"])                              # Fixing the different tf version model saving and loading issue. 
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        print(self.score)
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path = Path("scores.json"), data=scores)

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})

            if tracking_url_type_store != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="KDC_VGG16")
            else:
                mlflow.keras.log_model(self.model, "model")

