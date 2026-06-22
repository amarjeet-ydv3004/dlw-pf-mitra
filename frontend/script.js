const askBtn = document.getElementById("askBtn");
const userInput = document.getElementById("userInput");
const chatBox = document.getElementById("chatBox");

askBtn.addEventListener("click", async () => {

    const name = userInput.value;

    if(name.trim() === ""){
        alert("Please enter employee name");
        return;
    }

    // User Message
    chatBox.innerHTML += `
        <div class="user-message">
            ${name}
        </div>
    `;

    try {

        const response = await fetch(
            `http://127.0.0.1:5000/ask?name=${encodeURIComponent(name)}`
        );

        const data = await response.text();

        // Bot Message
        chatBox.innerHTML += `
            <div class="bot-message">
                ${data}
            </div>
        `;

    } catch(error){

        chatBox.innerHTML += `
            <div class="bot-message">
                Error connecting to server.
            </div>
        `;
    }

    userInput.value = "";

});