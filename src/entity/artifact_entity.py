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
