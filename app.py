import streamlit as st 
from src.synthetic_data_generator.config.configuration import ConfigurationManager
from src.synthetic_data_generator.logging.logger import logger 
from src.synthetic_data_generator.components.data_generator import DataGenerator
from src.synthetic_data_generator.utils.common import json_to_csv
import pandas as pd
import io
import json 

# Streamlit UI 
st.set_page_config(
    page_icon="📝",
    page_title="Synthetic Data Generator",
    layout = "wide"
)

st.title("🤖Synthetic Data Generator using LLM")
st.markdown("## Enter your shema and number of rows📃")

col1, col2 = st.columns([2,1])

with col1:
    schema_input = st.text_area(
        "Column Description (YAML or JSON format)",
        placeholder= "age: Age of an individual in years (integer)\ngender: Gender of individual ('M' or 'F')",
        height= 300
        )
    constraints_input = st.text_area(
            "Logical Constraints",
            placeholder="e.g., If age > 28, employment_status cannot be 'student'.",
            height=150
        )
with col2:
    num_rows = st.number_input(
        "Number of rows to generate",
        min_value = 1,
        value=10, 
        step = 1
    )

generate_button = st.button("Generate Data")

# Main logic 
if generate_button and schema_input:
    logger.info(f"User requested to generate {num_rows} rows.")

    with st.spinner("Generating data..."):
        try:
            # Initilize config manager 
            config_manager = ConfigurationManager()
            data_gen_config = config_manager.get_data_generation_config()

            # Initilize data generator with loaded config 
            generator = DataGenerator(config=data_gen_config)

            # generate JSON data from llm 
            json_data = generator.generate_data(schema = schema_input, 
                                                num_rows= num_rows, 
                                                constraints= constraints_input)
            logger.info("JSON object created successfully.")

            # Convert JSON to CSV 
            data = json.loads(json_data)
            if not isinstance(data, list):
                raise ValueError("LLM response is not a valid JSON list")
            
            df = pd.DataFrame(data)

            # Create an in-memory file for download 
            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False)
            csv_data = csv_buffer.getvalue().encode()

            st.success("CSV file generated successfully")
            logger.info("Data generated successfully. CSV file pepared for download")

            st.download_button(
                label = "Download CSV",
                data = csv_data,
                file_name = "synthetic_data.csv",
                mime="text/csv"
            )

            st.markdown("### Generated Data Preview")
            st.dataframe(df.head(5)) 

        except Exception as e:
            st.error(f"An error occured during data generation: {e}")
            logger.error(f"Data Generation failed: {e}")


