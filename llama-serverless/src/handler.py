import os
import runpod
from llama_cpp import Llama

# Get the directory where the current script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the model file
model_path = os.path.join(current_dir, "mistral-7b-instruct-v0.2.Q4_K_M.gguf")

args = {
    "model_path": model_path,
    "n_gpu_layers": -1
}

llm = Llama(**args)


def handler(event):
    inp = event["input"]
    return llm(**inp)


runpod.serverless.start({"handler": handler})
