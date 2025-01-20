# Update the entity so for that we are creating our own class
#entity is just the return type of a class.. so here we are creating our return type manually
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen= True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    update_base_model_path: Path
    params_image_size : list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int

@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir : Path
    tensorboard_root_log_dir : Path
    checkpoint_model_filepath: Path

    
@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list