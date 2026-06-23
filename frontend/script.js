const clearBtn = document.getElementById("clearBtn");
const askBtn = document.getElementById("askBtn");
const userInput = document.getElementById("userInput");
const chatBox = document.getElementById("chatBox");

// Ask Button Click
askBtn.addEventListener("click", async () => {

    const name = userInput.value.trim();

    if(name === ""){
        alert("Please enter a question");
        return;
    }

    // User Message
    chatBox.innerHTML += `
        <div class="user-message">
            ${name}
        </div>
    `;

    // Auto Scroll
    chatBox.scrollTop = chatBox.scrollHeight;

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

        // Auto Scroll
        chatBox.scrollTop = chatBox.scrollHeight;

    }
    catch(error){

        chatBox.innerHTML += `
            <div class="bot-message">
                ❌ Error connecting to server.
            </div>
        `;

        // Auto Scroll
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // Clear Input Box
    userInput.value = "";

});


// Enter Key Support
userInput.addEventListener("keypress", function(event){

    if(event.key === "Enter"){
        askBtn.click();
    }

});

clearBtn.addEventListener("click", () => {

    chatBox.innerHTML = `
        <div class="bot-message">
            Hello Amarjeet! 👋
            <br>
            Ask your PF related question.
        </div>
    `;

});