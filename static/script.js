async function sendMessage() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    const res = await fetch("/contact", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, email, message })
    });

    if (res.ok) {
        document.getElementById("status").innerText = "Message sent!";
    } else {
        document.getElementById("status").innerText = "Error sending message.";
    }
}
