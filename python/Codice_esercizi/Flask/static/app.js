document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: 'Hello from frontend' })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('data-container').innerText = data.message;
    });
});
