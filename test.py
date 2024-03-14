import subprocess
import time
import psutil
import GPUtil

# The command you want to run
command = "./realesrgan-ncnn-vulkan -i ./images/768x768.png -o 768x768.png "

# Start the timer
start_time = time.time()

# Run the command
process = subprocess.run(command, shell=True)

# Calculate the elapsed time
elapsed_time = time.time() - start_time

if process.returncode == 0:
    print(f"The command executed successfully and took {elapsed_time:.2f} seconds.")
else:
    print(f"The command failed with return code {process.returncode}.")
