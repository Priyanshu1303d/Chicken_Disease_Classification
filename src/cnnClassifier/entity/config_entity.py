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