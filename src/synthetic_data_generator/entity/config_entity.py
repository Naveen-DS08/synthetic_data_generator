from pathlib import Path 
from pydantic import BaseModel

class PathConfig(BaseModel):
    log_path: Path 
    output_path: Path 

class DataGeneratorConfig(BaseModel):
    model_name: str 
    temperature: float 
    json_mode: bool 
    prompt_template: str 
