import argparse
import yaml
import os
import importlib

from dataclasses import dataclass




# This function enables the user to select a configuration file while running the script, with the default set to './config/preprocess1_config.yaml'."
def parse_args():
    parser = argparse.ArgumentParser(description="Preprocess and transform data.")
    parser.add_argument('--configpath', default='./config/preprocess1_config.yaml', type=str, help='Path to the config file (YAML).')
    return parser.parse_args()




def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)


    # Load the base config (config0)
    base_config_path = config['base_config']
    with open(base_config_path, 'r') as base_file:
        base_config = yaml.safe_load(base_file)
    
    
    # copy base_config, merge with specific, then we will replace the {}
    merged_config = base_config.copy()
    for key, value in config['specific'].items():
        merged_config[key] = value
        
        

    # Replace placeholders by finding {{{key of base config}}} 
    for key, value in merged_config.items():
        if isinstance(value, str):
            for base_key, base_value in base_config.items():
                value = value.replace(f'{{{base_key}}}', base_value)
            merged_config[key] = value

    return merged_config



if __name__ == "__main__":
    args = parse_args()
    print(args)
    print(args.configpath)
    print()
    config = load_config(args.configpath)
    print(config)
