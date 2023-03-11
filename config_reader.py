import yaml


def read_config(config_file):

    with open(config_file, "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print("Read successful")
    return data
