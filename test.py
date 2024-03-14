import subprocess
import time
import psutil
import GPUtil

# List of commands you want to run
commands = [
    "./realesrgan-ncnn-vulkan -i ./images/768x768.png -o 768x768-animevideo.png -n realesr-animevideov3",
    "./realesrgan-ncnn-vulkan -i ./images/768x768.png -o 768x768-x4plus.png -n realesrgan-x4plus",
    "./realesrgan-ncnn-vulkan -i ./images/768x768.png -o 768x768-x4plusanime.png -n realesrgan-x4plus-anime",
    "./realesrgan-ncnn-vulkan -i ./images/600x600.png -o 600x600-animevideo.png -n realesr-animevideov3",
    "./realesrgan-ncnn-vulkan -i ./images/600x600.png -o 600x600-x4plus.png -n realesrgan-x4plus",
    "./realesrgan-ncnn-vulkan -i ./images/600x600.png -o 600x600-x4plusanime.png -n realesrgan-x4plus-anime",
]

# Iterate over the list of commands and execute them one by one
for command in commands:
    # Start the timer
    start_time = time.time()

    # Run the command
    process = subprocess.run(command, shell=True, check=True)

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Check the exit code and print the appropriate message
    if process.returncode == 0:
        print(f"The command executed successfully and took {elapsed_time:.2f} seconds.")
    else:
        print(f"The command failed with return code {process.returncode}.")
