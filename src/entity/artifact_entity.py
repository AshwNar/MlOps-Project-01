from dataclasses import dataclass
"""
This module defines data artifact entities used in the MLOps project.
Classes:
    DataIngestionArtifact: Stores file paths for the training and test datasets.
Notes:
    The @dataclass decorator automatically generates special methods such as __init__(), __repr__(), and __eq__() for the class,
    making it easier to create classes that are primarily used to store data.
Attributes:
    trained_file_path: Path to the file containing the training data.
    test_file_path: Path to the file containing the test data.
"""


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str

@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    validation_report_file_path: str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str
    transformed_train_file_path:str
    transformed_test_file_path:str
@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str 
    metric_artifact:ClassificationMetricArtifact

@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    changed_accuracy:float
    s3_model_path:str 
    trained_model_path:str

@dataclass
class ModelPusherArtifact:
    bucket_name:str
    s3_model_path:str