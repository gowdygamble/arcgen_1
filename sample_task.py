import visualize
import imp


task_filename = "./tasks\\diagonal_lines.py"


task_name = task_filename.split("\\")[-1]
task_name = task_name.split(".")[0]
print(task_name)

mod = imp.load_source(task_name, task_filename)
met = getattr(mod, "task_func")


input, output = met()
print(input)
print(output)
#visualize.visualize_canvas(input)
#visualize.visualize_canvas(output)
visualize.visualize_io_pair(input, output)


