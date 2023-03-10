import yaml


def read_config(config_file):

    with open("./configs/sample_config.yaml", "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print("Read successful")
    return data
