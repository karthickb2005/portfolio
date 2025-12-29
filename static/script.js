console.log("JS Loaded Successfully");

document.getElementById("uploadBtn").addEventListener("click", () => {

    const file = document.getElementById("resume").files[0];

    if (!file) {
        alert("Please choose a resume first!");
        return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        console.log("Response:", data);

        document.getElementById("name").innerText = data.name;
        document.getElementById("role").innerText = data.role;

        const skills = document.getElementById("skills");
        skills.innerHTML = "";
        data.skills.forEach(skill => {
            const li = document.createElement("li");
            li.textContent = skill;
            skills.appendChild(li);
        });
    })
    .catch(err => console.error("Error:", err));
});
