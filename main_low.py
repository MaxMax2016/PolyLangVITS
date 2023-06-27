import os
import subprocess
import sys

os.chdir('./datasets')
subprocess.run(["python", "integral_low.py", sys.argv[1], sys.argv[2], sys.argv[3]])

os.chdir('../')
subprocess.run(["python", "get_pretrained_model.py", sys.argv[1], sys.argv[2]])

config_path = f"../datasets/{sys.argv[2]}.json"
model_name = sys.argv[2]

os.chdir('./vits')
command = ["python", "train_ms.py", "-c", config_path, "-m", model_name]

subprocess.run(command)
