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


for command in commands:
    start_time = time.time()

    try:
        # Run the command and enforce checking for errors
        subprocess.run(command, shell=True, check=True)
        elapsed_time = time.time() - start_time
        print(f"The command executed successfully and took {elapsed_time:.2f} seconds.")
    except subprocess.CalledProcessError as e:
        # Handle the error for this command without stopping the script
        print(f"Failed to execute '{e.cmd}' with return code {e.returncode}.")
