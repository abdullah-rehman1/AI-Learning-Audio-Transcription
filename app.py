import whisper
import time

start_time = time.time()

# Replace with the path to your local model directory
model_path = "./whisper-models/base.pt"

# Load the model
model = whisper.load_model(model_path)  # Load the model on CPU

result = model.transcribe(r".\Audio-samples\positive.opus", language="ur", fp16=False) #fp16=False is required for CPU inference
transcribed_text = result["text"]
print(transcribed_text)

print("--- %s seconds ---" % (time.time() - start_time))
