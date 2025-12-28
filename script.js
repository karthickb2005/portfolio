function updateProfile() {
    const name = document.getElementById("nameInput").value;
    const role = document.getElementById("roleInput").value;
    const skill = document.getElementById("skillInput").value;
    const imageInput = document.getElementById("imageInput");

    if (name) localStorage.setItem("name", name);
    if (role) localStorage.setItem("role", role);
    if (skill) localStorage.setItem("skill", skill);

    if (imageInput.files.length > 0) {
        const reader = new FileReader();
        reader.onload = function () {
            localStorage.setItem("profileImage", reader.result);
            updateUI();
        };
        reader.readAsDataURL(imageInput.files[0]);
    }

    updateUI();
}

function updateUI() {
    const name = localStorage.getItem("name");
    const role = localStorage.getItem("role");
    const skill = localStorage.getItem("skill");
    const image = localStorage.getItem("profileImage");

    if (name) document.getElementById("name").innerText = name;
    if (role) document.getElementById("role").innerText = role;
    if (skill) document.getElementById("skill").innerText = skill;

    if (image) {
        const img = document.getElementById("profilePic");
        img.src = image;
        img.style.display = "block";
    }
}

window.onload = updateUI;
