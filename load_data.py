from glob import glob
from py_compile import main
import pandas as pd
import yaml
import os
import streamlit as st
from utlity import get_connection, close_connection, execute_query, insert_bulk_data


def load_yaml_data():
    # Define source and target folders
    conn = None
    try:
        data_dir = "C:\\Users\\Python\\datas"
        target_folder = "C:\\Users\\Python\\common_csv"
        os.makedirs(target_folder, exist_ok=True)

        yaml_files = glob(os.path.join(data_dir, '**', '*.yaml'), recursive=True)
        if not yaml_files:
            print("No YAML files found. Please check the directory path and file extensions.")
        else:
            os.makedirs(target_folder, exist_ok=True)
            print(f"Found {len(yaml_files)} YAML files.")
            symbol_data = {}
            for file in yaml_files:
                with open(file, 'r') as f:
                    data = yaml.safe_load(f)
                    for entry in data:
                        if 'Ticker' not in entry:
                            print(f"Skipping entry in {file}: {entry}")
                            continue
                        symbol = entry['Ticker']
                        if symbol not in symbol_data:
                            symbol_data[symbol] = []
                        symbol_data[symbol].append(entry)
            for symbol, entries in symbol_data.items():
                df = pd.DataFrame(entries)
                df.to_csv(os.path.join(target_folder, f'{symbol}.csv'), index=False)
                # Insert data into MySQL
                insert_bulk_data('stock_prices', entries)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        close_connection(conn)
        

if __name__ == "__main__":
    load_yaml_data()