from src.synthetic_data_generator.constants import *  
from src.synthetic_data_generator.utils.common import read_yaml, create_directories
from src.synthetic_data_generator.entity.config_entity import PathConfig, DataGeneratorCongig
from src.synthetic_data_generator.logging.logger import logger

class ConfigurationManager():
    "Manages all configuration"
    def __init__(self, 
             config_file_path = CONFIG_FILE_PATH,
             params_file_path = PARAMS_FILE_PATH, 
             prompt_template_file_path = PROMPT_TEMPLATE_FILE_PATH):
        try:
            self.config = read_yaml(config_file_path)
            self.params = read_yaml(params_file_path)
            self.prompt_template = read_yaml(prompt_template_file_path)
        except Exception as e:
            logger.error(f"Error loading configuration files: {e}")
            raise e

    def get_path_config(self) -> PathConfig:
        config = self.config.get("paths", {})

        # Create directories
        create_directories([config.get("log_path"), config.get("output_path")])
                
        path_config = PathConfig(
            log_path= config.get("log_path"),
            output_path = config.get("output_path")
        )
        return path_config
    
    def get_data_generation_config(self) -> DataGeneratorCongig:
        llm_params = self.params.get("llm", {})
        prompt_template = self.prompt_template.get("llm_prompt_template", "")

        data_gen_config = DataGeneratorCongig(
            model_name= llm_params.get("model_name"),
            temperature = llm_params.get("temperature"),
            json_mode = llm_params.get("json_model"),
            prompt_template = prompt_template
        )

        return data_gen_config
        
        
