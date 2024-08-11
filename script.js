const chatBox = document.getElementById('chat-box');
const messageInput = document.getElementById('message-input');
const userInfoForm = document.getElementById('user-info-form');
const botLogoURL = 'templates/caldigit_logo.jpg'; // Reference to the correct local logo file path

// Function to append a message to the chatbox
function appendMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);

    if (sender === 'bot') {
        const logoElement = document.createElement('img');
        logoElement.src = botLogoURL;
        logoElement.alt = 'Caldigit Logo';
        logoElement.classList.add('logo');
        logoElement.style.width = '30px'; // Adjust as needed
        logoElement.style.height = '30px'; // Adjust as needed

        const messageContent = document.createElement('div');
        messageContent.classList.add('message-content');
        messageContent.textContent = message;

        messageElement.appendChild(logoElement);
        messageElement.appendChild(messageContent);
    } else {
        messageElement.textContent = message;
    }

    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Function to send a message to the server and handle the response
async function sendMessage(message) {
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });
        const data = await response.json();
        if (data.message) {
            appendMessage('bot', data.message);
        } else {
            appendMessage('bot', 'Error: No response from chatbot.');
        }
    } catch (error) {
        appendMessage('bot', 'Error: Failed to communicate with chatbot.');
    }
}

// Function to start the chat after getting user information
function startChat() {
    const productName = document.getElementById('product-name').value;
    const issueDescription = document.getElementById('issue-description').value;

    if (productName.trim() && issueDescription.trim()) {
        appendMessage('bot', `Thank you! You are asking about the ${productName}. You mentioned: "${issueDescription}"`);
        userInfoForm.style.display = 'none';
        chatBox.style.display = 'block';
        messageInput.style.display = 'block';
        appendMessage('bot', 'How can I help you further?');
    } else {
        alert('Please fill out both fields.');
    }
}

// Event listener for the Enter key to send a message
messageInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        const userMessage = messageInput.value;
        if (userMessage.trim()) {
            appendMessage('user', userMessage);
            sendMessage(userMessage);
            messageInput.value = '';
        }
    }
});

// Append a welcome message when the page loads
window.onload = function() {
    appendMessage('bot', 'Welcome to the Caldigit Chatbot. Please provide the following information to get started.');
}
