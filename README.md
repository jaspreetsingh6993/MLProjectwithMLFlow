# MLProjectwithMLFlow

## Workflows
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/jaspreetsingh6993/MLProjectwithMLFlow
```
### STEP 01- Create a conda environment after opening the repository

conda create -p venv python==3.8 -y

conda activate venv/

### STEP 02- install the requirements
```cmd
pip install -r requirements.txt
```


```cmd
# Finally run the following command
python app.py
```

Now,
```cmd
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/jaspreetsingh6993/MLProjectwithMLFlow.mlflow \
MLFLOW_TRACKING_USERNAME=jaspreetsingh6993 \
MLFLOW_TRACKING_PASSWORD=7139c13710ddda433dc4b316e13d8d8b26520823 \
python script.py

Run this to set as env variables:

```cmd

set MLFLOW_TRACKING_URI=https://dagshub.com/jaspreetsingh6993/MLProjectwithMLFlow.mlflow

set MLFLOW_TRACKING_USERNAME=jaspreetsingh6993

set MLFLOW_TRACKING_PASSWORD=7139c13710ddda433dc4b316e13d8d8b26520823

```


