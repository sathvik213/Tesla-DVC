"""
Preprocessing module where the data transformation happens
"""

import os
import logging
import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

log_dir = 'logs'
Path('logs').mkdir(exist_ok=True)
# Setting up logger
logger = logging.getLogger('data_preprocessing')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'data_preprocessing.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def data_clean(data:pd.DataFrame,col_names:list)->pd.DataFrame:
  """ Dropping the duplicates if any"""
  try:
    data=data.drop(columns=col_names)
    logger.debug('Not needed columns removed')
    data=data.drop_duplicates(keep='first')
    return data
    logger.debug('Not needed columns removed')

  except Exception as e:
    logger.error('Error during the Cleaning Process: %s',e)


def graph_analysis(data:pd.DataFrame)->None:
  """Storing the calculcated graph """
  try:
    numeric_feature = data.select_dtypes(include = [np.number])
    c_data = numeric_feature.copy()
    c_data.hist(figsize = (20,20))
    plt.show()
    Path('artifacts').mkdir(exist_ok=True)
    plt.savefig("./artifacts/histograms.png")
    logger.debug('Histogram image saved successfully in artifacts folder')

    categorical_feature = data.select_dtypes(exclude=[np.number])
    categorical_feature['Model'].value_counts().plot.pie(figsize=(8,8), autopct='%1.1f%%')
    Path('artifacts').mkdir(exist_ok=True)
    plt.savefig("./artifacts/pie_chart.png")
    plt.show()
    logger.debug('Pie chart image saved successfully in artifacts folder')


    

  
  except Exception as e:
    logger.error('Failed to execute the graph analysis function : %s',e)
    

def main():
  """
  Main function to load the data from split sub folder and clean it
  """

  try:
    train_data=pd.read_csv('./data/split/train_data.csv')
    test_data=pd.read_csv('./data/split/test_data.csv')
    logger.debug('Data is has been successfully read from split subfolder')

    processed_train_data=data_clean(data=train_data,col_names=['Source_Type','Region'])
    processed_test_data=data_clean(data=test_data,col_names=['Source_Type','Region'])



    processed_data_path = Path('./data', 'processed')
    processed_data_path.mkdir(exist_ok=True)
    processed_data_str = str(processed_data_path)

    logger.debug('Path setting done for processed data')
    print(processed_data_path)
    train_data.to_csv(processed_data_path/'train_processed.csv',index=False)
    logger.debug('Trained data saved')

    test_data.to_csv(processed_data_path/'test_processed.csv',index=False)
    logger.debug('Test data saved')

    logger.debug('Saved the cleaned data to processed folder %s',processed_data_path)
    

    logger.debug('Saved the data to %s',processed_data_path)

    graph_analysis(train_data)
    logger.debug('Saved the graphs artifacts locally %s',processed_data_path)


  except Exception as e:
    logger.error('Failed to execute the preprocessing module: %s',e)
    print(f'{e}')

if __name__=='__main__':
  main() 

