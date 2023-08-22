
document.addEventListener('DOMContentLoaded', (event) => {
    // Code to interact with the AI assistant goes here

    // Example: Sending a message to the AI assistant
    const sendMessage = (message) => {
        fetch('/ai_assistant/api/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message }),
        })
        .then(response => response.json())
        .then(data => {
            // Handle the AI assistant's response here
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    };

    // Example: Receiving a message from the AI assistant
    const receiveMessage = () => {
        fetch('/ai_assistant/api/receive_message')
        .then(response => response.json())
        .then(data => {
            // Handle the AI assistant's message here
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    };
});
