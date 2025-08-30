from pathlib import Path 
from pydantic import BaseModel

class PathConfig(BaseModel):
    log_path: Path 
    output_path: Path 
