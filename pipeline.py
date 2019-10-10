import json
import tensorflow as tf
from utility import *
from sampler import *
from mapper import *
from optimizer import *


def main():

    # Step 1: Obtain config info from CLI
    data_path           = "./data/foo.edge"
    model_name          = "mf"
    config_path         = "./mf_setup.json"

    # Step 2: Load files, i.e., UI data and pipeline config, 
    edge_list           = load_data(data_path)
    model_config        = load_json(config_path)[model_name]

    print_json(model_config)

    print_json(edge_list)
    input()

    sampler_config      = model_config["sampler"]
    mapper_config       = model_config["mapper"]
    optimizer_config    = model_config["optimizer"]
   
    # Step 3: Assemble model pipeline
    sampler             = Sampler(sampler_config)
    mapper              = Mapper(mapper_config)
    optimizer           = Optimizer(optimizer_config)

    # Step 4: Evaluate model



if __name__ == "__main__":
    main()
