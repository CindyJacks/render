from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Hol den API-Key und die RAG Service URL aus den Umgebungsvariablen
API_KEY = os.getenv('API_KEY', 'ragflow-M4NDFjOWNjNzIxMDExZWY4Y2FkMDI0Mm')
RAG_SERVICE_URL = os.getenv('RAG_SERVICE_URL', 'http://localhost:5000/chat')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    # Hier wird der RAG-Service aufgerufen
    try:
        headers = {
            'Authorization': f'Bearer {API_KEY}',  # Füge den API-Key zu den Headers hinzu
            'Content-Type': 'application/json'
        }
        response = requests.post(RAG_SERVICE_URL, json={"message": user_input}, headers=headers)
        response_data = response.json()

        if response.status_code == 200:
            return jsonify(response_data)
        else:
            return jsonify({"error": f"RAG-Service responded with status code {response.status_code}"}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, port=port, host='0.0.0.0')
