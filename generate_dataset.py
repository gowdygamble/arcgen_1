from config_reader import read_config
import glob
import imp
import pickle

import visualize
from dataset_utils import tokenize_sample, tokenize_single


config_file = "./configs/sample_config.yaml"
config = read_config(config_file)

task_functions = glob.glob(config['task_folder'] + '/*.py')

x = []
y = []

for task_function in task_functions:

    task_name = task_function.split("\\")[-1]
    task_name = task_name.split(".")[0]
    print(task_name)

    mod = imp.load_source(task_name, task_function)
    met = getattr(mod, "task_func")

    for i in range(config['samples_per_task']):
        sample = []

        for ex in range(config['examples_per_sample']):
            inp, outp = met()
            sample.append(inp)
            sample.append(outp)

        # last example, for inference!
        inp_final, outp_final = met()
        sample.append(inp_final)

        tokenized_sample = tokenize_sample(sample)
        tokenized_target = tokenize_single(outp_final)

        #print(tokenized_sample)
        #print(len(tokenized_sample))
        #print("---")
        #print(tokenized_target)
        #print(len(tokenized_target))
        #print("==========")
        #visualize.visualize_io_pair(inp_final, outp_final)

        x.append(tokenized_sample)
        y.append(tokenized_target)



        #s = example_pair_to_tokens(inp, outp)
       
        



# try pickle first
print("writing x, y to files")
with open("x50k.pkl", 'wb') as f:
    pickle.dump(x, f)
with open("y50k.pkl", 'wb') as f:
    pickle.dump(y, f)
# then write as string
        