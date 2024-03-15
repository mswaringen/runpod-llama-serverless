# Serverless inference with Llama.cpp on RunPod

Runpod recently announced a new Dockerless deployment method using runpodctl, lets run an example.


From Repo
1. Clone repo locally
2. Install runpodctl
    1. Add API key
    2. Create network storage (10GB)
3. Wget model
    1. Modify model settings args in handler.py
4. Deploy

### Run server

`python3 -m llama_cpp.server --model models/mistral-7b-instruct-v0.2.Q4_K_M.gguf
--n_gpu_layers 35`



### Test

`curl -X 'POST' \
  'https://api.runpod.ai/v2/ihp7npv9uokvya/runsync' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": {}
}'`