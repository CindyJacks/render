function sendMessage() {
    let userInput = document.getElementById('userInput').value;

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    }).then(response => response.json())
      .then(data => {
          let messagesDiv = document.getElementById('messages');
          let userMessage = document.createElement('div');
          userMessage.innerHTML = "Du: " + userInput;
          messagesDiv.appendChild(userMessage);

          let botMessage = document.createElement('div');
          botMessage.innerHTML = "Bot: " + (data.message || data.error);
          messagesDiv.appendChild(botMessage);

          document.getElementById('userInput').value = '';
      });
}
