from config_reader import read_config
import glob
import imp

import visualize


config_file = "./configs/sample_config.yaml"
config = read_config(config_file)

task_functions = glob.glob(config['task_folder'] + '/*.py')
print(task_functions)

for task_function in task_functions:

    task_name = task_function.split("\\")[-1]
    task_name = task_name.split(".")[0]
    print(task_name)

    mod = imp.load_source(task_name, task_function)
    met = getattr(mod, "task_func")

    for i in range(config['samples_per_task']):
        i, o = met()
        visualize.visualize_io_pair(i, o)