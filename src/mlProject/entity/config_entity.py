from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Creating Data Ingestion Entity DataClass
    
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path