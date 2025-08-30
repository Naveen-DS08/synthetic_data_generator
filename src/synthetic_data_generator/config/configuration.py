from src.synthetic_data_generator.constants import *  
from src.synthetic_data_generator.utils.common import read_yaml
from src.synthetic_data_generator.entity.config_entity import PathConfig 
from src.synthetic_data_generator.utils.common import create_directories

class ConfigurationManager():
    def init(self, 
             config_file_path = CONFIG_FILE_PATH,
             params_file_path = PARAMS_FILE_PATH, 
             prompt_template_file_path = PROMPT_TEMPLATE_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.prompt_template = read_yaml(prompt_template_file_path)

    def get_path_config(self) -> PathConfig:
        config = self.config
        create_directories([config.log_path])
        create_directories([config.output_path])
        
        path_congig = PathConfig(
            log_path= config.log_path,
            output_path = config.output_path
        )
        
        
