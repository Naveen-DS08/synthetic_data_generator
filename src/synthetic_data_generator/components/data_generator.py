import os
import json 
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate 
from src.synthetic_data_generator.utils.common import * 
from src.synthetic_data_generator.logging import logger 
from src.synthetic_data_generator.entity.config_entity import DataGeneratorCongig 

from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

class DataGenerator:
    "Handles entire data generation process"
    def __init__(self, config: DataGeneratorCongig):
        self.config = config 
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        if not self.groq_api_key:
            logger.error("GROQ api key not found in environmental variables.")
            raise ValueError("GROQ api ket not set")
        
        # Initilize the llm 
        self.llm = ChatGroq(
            model= self.config.model_name,
            temperature = self.config.temperature,
            groq_api_key = self.groq_api_key
        )
    def generate_data(self, schema:str, num_rows:int) -> str:
        "Generates synthetic data bu prompting the llm"
        logger.info(f"Generating data with model: {self.config.model_name}")

        try:
            prompt_template = PromptTemplate(
                template= self.config.prompt_template,
                input_variables=["schema", "num_rows"]
            )

            prompt = prompt_template.format(schema=schema, num_rows=num_rows)

            if self.config.json_mode:
                response = self.llm.invoke(prompt, response_format={"type": "json_object"})
            else:
                response = self.llm.invoke(prompt)
            
            json_output = response.content
            logger.info("Successfully received response from LLM.")

            return json_output
        except Exception as e:
            logger.error(f"Error occured during generate data: {e}")
            raise Exception("Failed to generate data: {e}")


