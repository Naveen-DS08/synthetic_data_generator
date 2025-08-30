from pathlib import Path 
from pydantic import BaseModel

class PathConfig(BaseModel):
    log_path: Path 
    output_path: Path 

class DataGeneratorCongig(BaseModel):
    model_name: str 
    temperature: int 
    json_mode: bool 
    prompt_template: str 
