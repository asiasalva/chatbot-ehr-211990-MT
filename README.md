pip3 install -r requiremets.txt

py3 backend/main.py

npm run start

Used model to train the chatbot: bart-large https://huggingface.co/facebook/bart-large-mnli

Backend:
- analyze phrase passed by frontend using API
- check if it is a personal, general, or EHR information and controls other labels
- personal, general, and EHR information are taken from 3 different dictionaries
