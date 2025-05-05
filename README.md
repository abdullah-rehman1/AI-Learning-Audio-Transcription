# AI-Learning-Audio-Transcription

#### How to Run:

1. Ensure you have Python installed.
2. Navigate to your project directory **cd /path/to/your/project**
3. Create the environment named env **python -m venv env**
4. Activate the environment **.\env\Scripts\activate**
5. Install required modules using **pip install -r requirements.txt**
6. Run the application by executing the script using **python app.py**

#### Change the whisper model

1. Download desired model to local from <a>https://github.com/openai/whisper/blob/ba3f3cd54b0e5b8ce1ab3de13e32122d0d5f98ab/whisper/__init__.py#L17</a><br>
![image](https://github.com/user-attachments/assets/2feb3288-6fd5-4f4e-85c8-f203fdda01e0)

2. Store the .pt file in directory **\Sentiment Analysis from Voice\whisper-models**
3. Update the path in variable **model_path** inside app.py script<br>
   ![image](https://github.com/user-attachments/assets/b0347a8e-ffc2-4444-abda-a52da689bb11)
4. Run the application by executing the script using **python app.py**
