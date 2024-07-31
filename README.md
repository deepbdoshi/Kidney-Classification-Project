# Kidney-Classification-Project


## Things to add:-
* Template creation for folder structure for projects
* Github setup - token creation
* Setup.py for pypy module.
* Environment setup and activation
* Installing the requirements
* Adding the venv dir to gitignore
* Logger functionality in the constructor file to optimize importing the packages
* Config Box and Ensure Annotations.
* Project Workflows
* Config.YAML file updating
* Understanding Entity
* 


## Workflows
* Update config.yaml    --> holds the configs for data downloading.
* Update secrets.yaml [Optional]
* Update params.yaml    --> empty as of now
* Update the entity     --> 
* Update the configuration manager in src config
* Update the components
* Update the pipeline
* Update the main.py
* Update the dvc.yaml
* app.py

## Commands
* kidney-disease-clf\Scripts\activate.bat
* deactivate

## ML-Flow Commands
* set MLFLOW_TRACKING_USERNAME=SUPREME-CODER
* set MLFLOW_TRACKING_URI=https://dagshub.com/SUPREME-CODER/Kidney-Classification-Project.mlflow
* set MLFLOW_TRACKING_PASSWORD=Deep@161299

## ML-Flow Code
```
import dagshub
dagshub.init(repo_owner='SUPREME-CODER', repo_name='Kidney-Classification-Project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
```