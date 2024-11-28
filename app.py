from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Hol den API-Key aus der Umgebungsvariable
API_KEY = os.getenv('API_KEY', 'default_value')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    # Hier könntest du die Logik zur Bearbeitung der Anfrage implementieren
    # Anstatt eine andere URL aufzurufen, kannst du z.B. direkt eine Antwort generieren:
    response_data = {
        "message": f"Deine Eingabe war: {user_input}"  # Hier einfaches Echo als Beispiel
    }
    return jsonify(response_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, port=port, host='0.0.0.0')
