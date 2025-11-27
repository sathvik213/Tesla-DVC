"""code for data ingestion technique
"""



import pandas as pd
import os
from sklearn.model_selection import train_test_split
import logging

os.makedirs('logs',exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler("logs/data_ingestion.log", mode="a", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("{asctime} - {levelname} - {message}", style="{")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def load_data(url_path:str)->pd.DataFrame:
    """Loading of the data from URL and returning back"""
    try: 
        
        df=pd.read_csv(url_path)
        return df

    except OSError as e:
        logger.debug("OSError has occured due to %s, solution can be to add 'r' before url to read",e)
    except Exception as e:
        logger.debug('Cant be executed due to %s',e)


def save_data(train_data:pd.DataFrame,test_data:pd.DataFrame)->None:
    """Function to save the data to the split group for future use"""
    try:
        path='data\split'
        os.makedirs(path)
        print(train_data.shape)
        print(test_data.shape)
        train_data.to_csv(os.path.join(path,'train_data.csv'))
        test_data.to_csv(os.path.join(path,'test_data.csv'))
        logger.debug('data is now saved at %s',path)

    except Exception as e:
        logger.debug('Failed to save the data  %s',e)

def load_params(params_path:str)->dict:
    """Function to load the parameters from YAML file"""
    try:
        import yaml
        with open(params_path, 'r') as file:
                    # print(file)
                    params=yaml.safe_load(file)
        logger.debug('Params are loaded')
        return params
    except Exception as e:
        logger.debug('Params dictionary file not pulled properly  %s',e)

def main():
    """Entry point of data ingestion code execution"""
    FIXED_STATE=101
    try:
        params=load_params(params_path='params.yml')
        test_size=params['data_ingestion']['test_size']
        # print(os.getcwd())
        url_path=r"data\raw\tesla_deliveries_dataset_2015_2025.csv"
        df=load_data(url_path)
        train_data,test_data=train_test_split(df,test_size=test_size,random_state=FIXED_STATE)

        save_data(train_data,test_data)
        logger.debug('Splitted data i.e.train and test are now saved ')


    
    except Exception as e:
        logger.debug('Failed to execute the data ingestion module  %s',e)




if __name__=='__main__':
    main()
# def load_params(params_path: str) -> dict:
#     """Load parameters from a YAML file."""
#     try:
#         with open(params_path, 'r') as file:
#             params = yaml.safe_load(file)
#         logger.debug('Parameters retrieved from %s', params_path)
#         return params
#     except FileNotFoundError:
#         logger.error('File not found: %s', params_path)
#         raise
#     except yaml.YAMLError as e:
#         logger.error('YAML error: %s', e)
#         raise
#     except Exception as e:
#         logger.error('Unexpected error: %s', e)
#         raise

# def load_data(data_url:str)-> pd.DataFrame:

#     try:
#       df=pd.read_csv(data_url)
#       logger.debug('Data loaded from %s',data_url)
#       return df
#     except pd.errors.ParserError as e:
#       logger.error('Failed to parse the cs vfile : %s',e)
#     except Exception as e:
#       logger.error('Unexpected error occurred while loading the data: %s',e)
#       raise

# def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
#     """Preprocess the data."""
#     try:
#         df.drop(columns = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace = True)
#         df.rename(columns = {'v1': 'target', 'v2': 'text'}, inplace = True)
#         logger.debug('Data preprocessing completed')
#         return df
#     except KeyError as e:
#         logger.error('Missing column in the dataframe: %s', e)
#         raise
#     except Exception as e:
#         logger.error('Unexpected error during preprocessing: %s', e)
#         raise

# def save_data(train_data: pd.DataFrame, test_data: pd.DataFrame, data_path: str) -> None:
#     """Save the train and test datasets."""
#     try:
#         raw_data_path = os.path.join(data_path, 'raw')
#         os.makedirs(raw_data_path, exist_ok=True)
#         train_data.to_csv(os.path.join(raw_data_path, "train.csv"), index=False)
#         test_data.to_csv(os.path.join(raw_data_path, "test.csv"), index=False)
#         logger.debug('Train and test data saved to %s', raw_data_path)
#     except Exception as e:
#         logger.error('Unexpected error occurred while saving the data: %s', e)
#         raise



