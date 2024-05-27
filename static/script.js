const chatForm = document.getElementById('chat-form');
const chatHistory = document.querySelector('.chat-history');
const userInputField = document.querySelector('input[name="user_input"]');

function appendMessage(message, className) {
  const messageElement = document.createElement('div');
  messageElement.classList.add(className);
  messageElement.innerText = message;
  chatHistory.appendChild(messageElement);
  chatHistory.scrollTop = chatHistory.scrollHeight;  // Auto-scroll to the bottom
}

chatForm.addEventListener('submit', function(event) {
  event.preventDefault();

  const userInput = userInputField.value.trim();
  if (userInput === '') {
    return;
  }

  appendMessage(userInput, 'user-message');
  userInputField.value = '';  // Clear the input field after sending

  // Send user input to the backend (Flask app) using AJAX
  fetch('/process', {
    method: 'POST',
    body: JSON.stringify({ user_input: userInput }),
    headers: { 'Content-Type': 'application/json' }
  })
  .then(response => response.json())
  .then(data => {
    const responseText = data.text;
    appendMessage(responseText, 'ella-message');

    // Access the audio file path from the data object
    const audioFilePath = data.audio_file;

    // Play the audio using HTML5 Audio API (assuming browser support)
    const audioElement = new Audio(audioFilePath);
    audioElement.play();
  })
  
  .catch(error => {
    console.error('Error fetching response:', error);
    appendMessage('An error occurred. Please try again later.', 'error-message');
  });
});

// Handle suggestion prompts (assuming they trigger sending the prompt as user input)
const suggestionPrompts = document.querySelectorAll('.suggestion-prompts span');

suggestionPrompts.forEach(prompt => {
  prompt.addEventListener('click', function() {
    userInputField.value = prompt.textContent.trim();
    chatForm.submit();
  });
});
