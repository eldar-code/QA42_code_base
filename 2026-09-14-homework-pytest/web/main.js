function toggleSecretMessage() {
    const msg = document.getElementById("secret-message");
    const btn = document.getElementById("toggle-btn");
    
    if (msg.classList.contains("hidden")) {
        msg.classList.remove("hidden");
        btn.textContent = "Hide Message";
    } else {
        msg.classList.add("hidden");
        btn.textContent = "Show Message";
    }
}

function updateTitleText() {
    const inputVal = document.getElementById("user-input").value;
    const heading = document.getElementById("dynamic-heading");
    if (inputVal.trim() !== "") {
        heading.textContent = inputVal;
    }
}

function filterTable() {
    const input = document.getElementById("table-search");
    const filter = input.value.toLowerCase();
    const table = document.getElementById("users-table");
    const tr = table.getElementsByTagName("tr");
    let visibleCount = 0;

    for (let i = 1; i < tr.length; i++) {
        const tdName = tr[i].getElementsByTagName("td")[2];
        if (tdName) {
            const txtValue = tdName.textContent || tdName.innerText;
            if (txtValue.toLowerCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
                visibleCount++;
            } else {
                tr[i].style.display = "none";
            }
        }
    }
    document.getElementById("row-counter").textContent = `Total Rows: ${visibleCount}`;
}

function handleFormSubmit(event) {
    event.preventDefault();
    const name = document.getElementById("full-name").value;
    const terms = document.getElementById("terms-check").checked;
    const statusMsg = document.getElementById("status-message");

    if (!terms) {
        statusMsg.style.color = "red";
        statusMsg.textContent = "Error: You must accept the terms!";
        return;
    }

    statusMsg.style.color = "green";
    statusMsg.textContent = `Success: Thank you ${name}, registration complete!`;
}