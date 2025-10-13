# AI CLIENT
import requests
import json
import time
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class AIClient:
    def __init__(self, api_key, base_url="https://api.example.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _handle_response(self, response):
        if response.status_code != 200:
            logger.error(f"API request failed with status code {response.status_code}: {response.text}")
            response.raise_for_status()
        return response.json()

    def generate_text(self, prompt, model="gpt-4", max_tokens=150):
        url = f"{self.base_url}/generate"
        payload = {
            "model": model,
            "prompt": prompt,
            "max_tokens": max_tokens
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        return self._handle_response(response)

    def upload_file(self, file_path):
        url = f"{self.base_url}/upload"
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(url, headers={"Authorization": f"Bearer {self.api_key}"}, files=files)
        return self._handle_response(response)

    def get_file_info(self, file_id):
        url = f"{self.base_url}/files/{file_id}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def delete_file(self, file_id):
        url = f"{self.base_url}/files/{file_id}"
        response = requests.delete(url, headers=self.headers)
        return self._handle_response(response)
    def list_files(self):
        url = f"{self.base_url}/files"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)
    def create_embedding(self, text, model="text-embedding-ada-002"):
        url = f"{self.base_url}/embeddings"
        payload = {
            "model": model,
            "input": text
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        return self._handle_response(response)
    def chat(self, messages, model="gpt-4", max_tokens=150):
        url = f"{self.base_url}/chat"
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        return self._handle_response(response)
    def fine_tune(self, training_file_id, model="gpt-4", n_epochs=4):
        url = f"{self.base_url}/fine-tunes"
        payload = {
            "model": model,
            "training_file": training_file_id,
            "n_epochs": n_epochs
        }
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        return self._handle_response(response)
    def get_fine_tune_status(self, fine_tune_id):
        url = f"{self.base_url}/fine-tunes/{fine_tune_id}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)
    def cancel_fine_tune(self, fine_tune_id):
        url = f"{self.base_url}/fine-tunes/{fine_tune_id}/cancel"
        response = requests.post(url, headers=self.headers)
        return self._handle_response(response)
    def list_fine_tunes(self):
        url = f"{self.base_url}/fine-tunes"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)
    def download_file(self, file_id, destination_path):
        url = f"{self.base_url}/files/{file_id}/download"
        response = requests.get(url, headers=self.headers, stream=True)
        if response.status_code == 200:
            with open(destination_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            logger.info(f"File downloaded successfully to {destination_path}")
        else:
            self._handle_response(response)
# Example usage:
if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    client = AIClient(api_key)
    prompt = "Once upon a time"
    response = client.generate_text(prompt)
    print(response)
# AI CLIENT